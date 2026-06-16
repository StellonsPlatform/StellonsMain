import 'package:flutter/material.dart';

class WorkflowNodeCard extends StatelessWidget {
  final String title;
  final String agent;
  final String status;

  const WorkflowNodeCard({
    super.key,
    required this.title,
    required this.agent,
    required this.status,
  });

  Color getStatusColor() {
    switch (status.toLowerCase()) {
      case "completed":
        return Colors.green;
      case "running":
        return Colors.orange;
      case "pending":
        return Colors.grey;
      default:
        return Colors.blue;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 400,
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade300),
        boxShadow: [
          BoxShadow(color: Colors.black.withOpacity(0.05), blurRadius: 10),
        ],
      ),
      child: Column(
        children: [
          Text(
            agent,
            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 10),

          Text(title, style: const TextStyle(fontSize: 16)),

          const SizedBox(height: 12),

          Chip(
            backgroundColor: getStatusColor(),
            label: Text(status, style: const TextStyle(color: Colors.white)),
          ),
        ],
      ),
    );
  }
}
