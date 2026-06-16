import 'package:flutter/material.dart';

class PromptBar extends StatelessWidget {
  final TextEditingController controller;
  final VoidCallback onGenerate;

  const PromptBar({
    super.key,
    required this.controller,
    required this.onGenerate,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),

      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border(bottom: BorderSide(color: Color(0xFFE5E7EB))),
      ),

      child: Row(
        children: [
          Expanded(
            child: TextField(
              controller: controller,

              decoration: InputDecoration(
                hintText: "Create AKS cluster in East US with 3 nodes",

                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
              ),
            ),
          ),

          const SizedBox(width: 16),

          ElevatedButton.icon(
            onPressed: onGenerate,

            icon: const Icon(Icons.auto_awesome),

            label: const Text("Generate Architecture"),
          ),
        ],
      ),
    );
  }
}
