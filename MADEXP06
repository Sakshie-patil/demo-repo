import 'package:flutter/material.dart';

void main() {
  runApp(MyNavigationApp());
}

class MyNavigationApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Navigation and Gesture Demo',
      routes: {
        '/': (context) => HomePage(),
        '/second': (context) => SecondPage(),
      },
      initialRoute: '/',
    );
  }
}

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String _gestureStatus = 'Perform a gesture';

  void _updateStatus(String status) {
    setState(() {
      _gestureStatus = status;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home Page with Navigation and Gestures'),
        backgroundColor: Colors.blue,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(
              'Welcome to the Home Page!',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Text(
              'Tap the button below to navigate to the second page. Also, try the gestures!',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 20),
            GestureDetector(
              onTap: () => _updateStatus('Tapped!'),
              onDoubleTap: () => _updateStatus('Double Tapped!'),
              onLongPress: () => _updateStatus('Long Pressed!'),
              onHorizontalDragUpdate: (_) =>
                  _updateStatus('Horizontal Dragging...'),
              child: Container(
                width: 200,
                height: 200,
                decoration: BoxDecoration(
                  color: Colors.orangeAccent,
                  borderRadius: BorderRadius.circular(16),
                ),
                alignment: Alignment.center,
                child: Text(
                  'Touch Me!',
                  style: TextStyle(fontSize: 22, color: Colors.white),
                ),
              ),
            ),
            SizedBox(height: 30),
            Text(
              _gestureStatus,
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/second');
              },
              child: Text('Go to Second Page'),
            ),
          ],
        ),
      ),
    );
  }
}

class SecondPage extends StatefulWidget {
  @override
  _SecondPageState createState() => _SecondPageState();
}

class _SecondPageState extends State<SecondPage> {
  String _gestureStatus = 'Perform a gesture';

  void _updateStatus(String status) {
    setState(() {
      _gestureStatus = status;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Second Page with Gestures'),
        backgroundColor: Colors.green,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Text(
              'This is the Second Page!',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            GestureDetector(
              onTap: () => _updateStatus('Tapped!'),
              onDoubleTap: () => _updateStatus('Double Tapped!'),
              onLongPress: () => _updateStatus('Long Pressed!'),
              onHorizontalDragUpdate: (_) =>
                  _updateStatus('Horizontal Dragging...'),
              child: Container(
                width: 200,
                height: 200,
                decoration: BoxDecoration(
                  color: Colors.orangeAccent,
                  borderRadius: BorderRadius.circular(16),
                ),
                alignment: Alignment.center,
                child: Text(
                  'Touch Me!',
                  style: TextStyle(fontSize: 22, color: Colors.white),
                ),
              ),
            ),
            SizedBox(height: 30),
            Text(
              _gestureStatus,
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
            ),
            SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                Navigator.pop(context); // Go back to the Home Page
              },
              child: Text('Back to Home'),
            ),
          ],
        ),
      ),
    );
  }
}
