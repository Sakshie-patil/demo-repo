import 'package:flutter/material.dart';

void main() {
  runApp(MyLayoutApp());
}

class MyLayoutApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Layout Example',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Layout Widgets Demo'),
          backgroundColor: Colors.deepPurple,
        ),
        body: Column(
          children: [
            // Header section
            Container(
              width: double.infinity,
              padding: EdgeInsets.all(16),
              color: Colors.deepPurple.shade100,
              child: Center(
                child: Text(
                  'Welcome to My App!',
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                ),
              ),
            ),

            SizedBox(height: 20),

            // Main content using Row and Expanded
            Expanded(
              child: Row(
                children: [
                  // Left panel
                  Expanded(
                    child: Container(
                      color: Colors.amber[200],
                      child: Center(child: Text('Left Panel')),
                    ),
                  ),
                  // Main content area
                  Expanded(
                    flex: 2,
                    child: Container(
                      color: Colors.green[100],
                      child: Center(child: Text('Main Content')),
                    ),
                  ),
                  // Right panel
                  Expanded(
                    child: Container(
                      color: Colors.amber[200],
                      child: Center(child: Text('Right Panel')),
                    ),
                  ),
                ],
              ),
            ),

            // Footer section
            Container(
              width: double.infinity,
              padding: EdgeInsets.all(16),
              color: Colors.deepPurple.shade200,
              child: Center(
                child: Text(
                  'Footer Area',
                  style: TextStyle(fontSize: 18, color: Colors.white),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
