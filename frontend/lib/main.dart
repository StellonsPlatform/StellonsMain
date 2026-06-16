import 'package:flutter/material.dart';

import 'shell/stellons_shell.dart';

void main() {
  runApp(const StellonsApp());
}

class StellonsApp extends StatelessWidget {
  const StellonsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Stellons',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: Colors.white,
      ),
      home: const StellonsShell(),
    );
  }
}
