@app.route('/generate_answers', methods=['POST'])
@rate_limit_decorator
def generate_answers():
    try:
        questions = session.get('questions', [])
        job_title = session.get('job_title', '')
        resume_text = session.get('resume_text', '')
        
        if not questions:
            return jsonify({'error': 'No questions found. Please generate questions first.'})
        
        api_key = os.environ.get('GEMINI_API_KEY')
        if not api_key:
            return jsonify({'error': 'API key not configured on server.'})
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Process each question individually to guarantee all answers
        answers = {}
        
        for i, question in enumerate(questions[:10], 1):
            try:
                # Individual prompt for each question
                prompt = f"""
Generate a STAR method answer for this interview question:

Job Title: {job_title}
Resume Context: {resume_text[:500]}

Question {i}: {question}

Provide your answer in this EXACT format:
SITUATION: [Brief description of the situation - 1-2 sentences]
TASK: [What needed to be accomplished - 1 sentence]  
ACTION: [Specific actions you took - 1-2 sentences]
RESULT: [The outcome achieved - 1 sentence]

Make it professional and relevant to the job title. Do not include any other text or formatting.
"""
                
                @retry_gemini_api()
                def generate_single_answer(model, prompt):
                    return model.generate_content(prompt)
                
                response = generate_single_answer(model, prompt)
                
                # Parse the individual response
                answer_text = response.text.strip()
                formatted_answer = parse_single_answer(answer_text)
                
                answers[i] = formatted_answer
                
                # Small delay to avoid rate limiting
                import time
                time.sleep(0.3)
                
            except Exception as e:
                print(f"Error generating answer for question {i}: {str(e)}")
                # Create fallback answer to maintain order
                answers[i] = create_fallback_answer(question, job_title, i)
        
        # Final check - ensure we have exactly 10 answers in order
        final_answers = {}
        for i in range(1, 11):
            if i in answers:
                final_answers[i] = answers[i]
            else:
                # Create missing answer
                question_text = questions[i-1] if i <= len(questions) else "General interview question"
                final_answers[i] = create_fallback_answer(question_text, job_title, i)
        
        return jsonify({
            'success': True,
            'structured_answers': final_answers,
            'total_questions': 10,
            'method_used': 'STAR Method'
        })
        
    except google.api_core.exceptions.ResourceExhausted as e:
        return jsonify({'error': "API quota exceeded for answer generation. Please check your Google Cloud Console for usage limits or try again later."})
    except google.api_core.exceptions.GoogleAPIError as e:
        return jsonify({'error': f"Google API error during answer generation: {str(e)}. Please try again."})
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred during answer generation: {str(e)}'})

def parse_single_answer(answer_text):
    """Parse a single answer response"""
    import re
    
    # Initialize components
    situation = ""
    task = ""
    action = ""
    result = ""
    
    # Split by lines and process
    lines = answer_text.split('\n')
    current_section = None
    current_content = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section headers
        if re.match(r'^SITUATION:', line, re.IGNORECASE):
            if current_section and current_content:
                save_section_content(current_section, current_content, locals())
            current_section = 'situation'
            current_content = [line.split(':', 1)[1].strip() if ':' in line else '']
            
        elif re.match(r'^TASK:', line, re.IGNORECASE):
            if current_section and current_content:
                save_section_content(current_section, current_content, locals())
            current_section = 'task'
            current_content = [line.split(':', 1)[1].strip() if ':' in line else '']
            
        elif re.match(r'^ACTION:', line, re.IGNORECASE):
            if current_section and current_content:
                save_section_content(current_section, current_content, locals())
            current_section = 'action'
            current_content = [line.split(':', 1)[1].strip() if ':' in line else '']
            
        elif re.match(r'^RESULT:', line, re.IGNORECASE):
            if current_section and current_content:
                save_section_content(current_section, current_content, locals())
            current_section = 'result'
            current_content = [line.split(':', 1)[1].strip() if ':' in line else '']
            
        else:
            # Continue current section
            if current_section:
                current_content.append(line)
    
    # Save the last section
    if current_section and current_content:
        save_section_content(current_section, current_content, locals())
    
    # If parsing failed, try simple extraction
    if not situation and not task and not action and not result:
        situation, task, action, result = extract_star_simple(answer_text)
    
    # Format for HTML display
    formatted_answer = f"""
<strong>Situation:</strong> {situation or 'Relevant professional situation from my experience.'}<br>
<strong>Task:</strong> {task or 'Clear objective that needed to be accomplished.'}<br>
<strong>Action:</strong> {action or 'Systematic approach and specific steps taken.'}<br>
<strong>Result:</strong> {result or 'Successful outcome with measurable impact.'}
"""
    
    return formatted_answer.strip()

def save_section_content(section, content_list, local_vars):
    """Helper function to save section content"""
    content = ' '.join(content_list).strip()
    if content:
        local_vars[section] = content

def extract_star_simple(text):
    """Simple extraction as fallback"""
    import re
    
    situation = ""
    task = ""
    action = ""
    result = ""
    
    # Try to find each component with regex
    sit_match = re.search(r'situation[:\-\s]+(.*?)(?=task|action|result|$)', text, re.IGNORECASE | re.DOTALL)
    if sit_match:
        situation = sit_match.group(1).strip()
    
    task_match = re.search(r'task[:\-\s]+(.*?)(?=action|result|situation|$)', text, re.IGNORECASE | re.DOTALL)
    if task_match:
        task = task_match.group(1).strip()
    
    action_match = re.search(r'action[:\-\s]+(.*?)(?=result|situation|task|$)', text, re.IGNORECASE | re.DOTALL)
    if action_match:
        action = action_match.group(1).strip()
    
    result_match = re.search(r'result[:\-\s]+(.*?)(?=situation|task|action|$)', text, re.IGNORECASE | re.DOTALL)
    if result_match:
        result = result_match.group(1).strip()
    
    return situation, task, action, result

def create_fallback_answer(question, job_title, question_num):
    """Create a structured fallback answer"""
    
    # Create contextual fallback based on question content
    question_lower = question.lower()
    
    if 'challenge' in question_lower or 'difficult' in question_lower:
        situation = f"In my role as a {job_title}, I encountered a challenging situation that required immediate attention."
        task = "I needed to resolve the issue while maintaining quality standards and meeting deadlines."
        action = "I analyzed the problem systematically, consulted with relevant stakeholders, and implemented a step-by-step solution."
        result = "The challenge was successfully resolved, and I gained valuable experience for handling similar situations."
        
    elif 'team' in question_lower or 'collaborate' in question_lower:
        situation = f"While working as a {job_title}, I was part of a diverse team working on an important project."
        task = "I needed to ensure effective collaboration and contribute to achieving our team objectives."
        action = "I actively participated in team discussions, shared my expertise, and supported colleagues when needed."
        result = "Our team successfully completed the project on time and received positive feedback from stakeholders."
        
    elif 'learn' in question_lower or 'new' in question_lower:
        situation = f"In my position as a {job_title}, I encountered a situation requiring skills I hadn't used before."
        task = "I needed to quickly acquire new knowledge and apply it effectively to meet project requirements."
        action = "I dedicated time to research, sought guidance from experts, and practiced the new skills systematically."
        result = "I successfully mastered the new skills and applied them to deliver quality results."
        
    else:
        # Generic fallback
        situation = f"During my experience as a {job_title}, I faced a situation that required professional judgment and action."
        task = "I needed to address the situation effectively while maintaining high standards."
        action = "I approached the challenge methodically, gathered necessary information, and implemented appropriate solutions."
        result = "The situation was resolved successfully, contributing to positive outcomes for the organization."
    
    return f"""
<strong>Situation:</strong> {situation}<br>
<strong>Task:</strong> {task}<br>
<strong>Action:</strong> {action}<br>
<strong>Result:</strong> {result}
"""
