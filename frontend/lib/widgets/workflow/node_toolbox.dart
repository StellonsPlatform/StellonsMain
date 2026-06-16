import 'package:flutter/material.dart';

class NodeToolbox extends StatelessWidget {
  const NodeToolbox({super.key});

  Widget draggableNode(String title) {
    return Draggable<String>(
      data: title,

      feedback: Material(
        color: Colors.transparent,
        child: Container(
          width: 160,
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(14),
            boxShadow: const [BoxShadow(blurRadius: 12, color: Colors.black12)],
          ),
          child: Text(
            title,
            style: const TextStyle(fontWeight: FontWeight.w600),
          ),
        ),
      ),

      childWhenDragging: Opacity(opacity: 0.35, child: toolboxCard(title)),

      child: toolboxCard(title),
    );
  }

  Widget toolboxCard(String title) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.grey.shade300),
      ),
      child: Text(title, style: const TextStyle(fontSize: 14)),
    );
  }

  Widget sectionTitle(String title) {
    return Padding(
      padding: const EdgeInsets.only(top: 10, bottom: 12),
      child: Text(
        title,
        style: TextStyle(
          fontWeight: FontWeight.bold,
          fontSize: 14,
          color: Colors.grey.shade700,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 220,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: const [BoxShadow(blurRadius: 12, color: Colors.black12)],
      ),

      child: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              "Components",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 20),

            sectionTitle("Agents"),

            draggableNode("Planner"),
            draggableNode("Azure"),
            draggableNode("AWS"),

            const SizedBox(height: 12),

            sectionTitle("Resources"),

            draggableNode("Resource Group"),
            draggableNode("Virtual Network"),
            draggableNode("AKS Cluster"),
            draggableNode("Storage Account"),
            draggableNode("Key Vault"),
            draggableNode("Database"),
            draggableNode("Monitoring"),
            draggableNode("Container Registry"),

            const SizedBox(height: 12),

            sectionTitle("AI"),

            draggableNode("AI Model"),
            draggableNode("LLM Router"),
            draggableNode("Embedding Model"),
          ],
        ),
      ),
    );
  }
}
