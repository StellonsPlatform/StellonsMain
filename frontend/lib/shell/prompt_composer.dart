import 'package:flutter/material.dart';

class PromptComposer extends StatelessWidget {
  const PromptComposer({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(20),
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          border: Border.all(color: Colors.grey.shade300),
          borderRadius: BorderRadius.circular(16),
        ),
        child: const Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("+ Configure Smartly", style: TextStyle(color: Colors.grey)),

            SizedBox(height: 20),

            Row(
              children: [
                Chip(label: Text("Context: US Central")),

                Spacer(),

                CircleAvatar(radius: 18, child: Icon(Icons.arrow_upward)),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
