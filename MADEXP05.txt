To include icons, images, and charts, you need to add the necessary dependencies in your pubspec.yaml file.

Open pubspec.yaml in your project and make the following changes:
Add the following dependencies for charts (e.g., fl_chart):
dependencies:
  flutter:
    sdk: flutter
  fl_chart: ^0.40.0  # Add this line for charts
Ensure Image and Icon Assets are Included:
Make sure you have added the images (icons or custom images) in an assets directory and referenced them in pubspec.yaml:
flutter:
  assets:
    - assets/images/  # Path where your images are stored
Run flutter pub get in the terminal to install the dependencies.


      // code 

      
import 'package:flutter/material.dart';
import 'package:fl_chart/fl_chart.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Flutter Icons, Images, and Charts')),
      body: SingleChildScrollView(
        child: Column(
          children: [
            // Display Material Icon
            Icon(Icons.home, size: 50, color: Colors.blue),
            
            // Display Custom Image from assets
            Image.asset('assets/images/sample_image.png', width: 200),
            
            // Display Bar Chart
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: BarChart(
                BarChartData(
                  titlesData: FlTitlesData(show: false),
                  borderData: FlBorderData(show: false),
                  barGroups: [
                    BarChartGroupData(x: 0, barRods: [BarChartRodData(y: 8, colors: [Colors.blue])]),
                    BarChartGroupData(x: 1, barRods: [BarChartRodData(y: 10, colors: [Colors.green])]),
                    BarChartGroupData(x: 2, barRods: [BarChartRodData(y: 6, colors: [Colors.red])]),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
