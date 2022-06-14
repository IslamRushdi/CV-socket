import 'package:camera_app/screens/OCR_app.dart';
import 'package:camera_app/screens/stt_screen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: OCRapp(),
      // home: SearchForObject(),
    );
  }
}
