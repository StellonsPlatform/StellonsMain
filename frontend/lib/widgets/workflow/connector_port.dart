import 'package:flutter/material.dart';

class ConnectorPort extends StatelessWidget {
  final Color color;
  final VoidCallback onTap;

  const ConnectorPort({super.key, required this.color, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: 18,
        height: 18,
        decoration: BoxDecoration(
          color: color,
          shape: BoxShape.circle,
          border: Border.all(color: Colors.white, width: 3),
          boxShadow: [BoxShadow(color: color.withAlpha(100), blurRadius: 8)],
        ),
      ),
    );
  }
}
