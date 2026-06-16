import 'package:flutter/material.dart';
import 'task_card.dart';

class TaskPanel extends StatelessWidget {
  const TaskPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 320,
      padding: const EdgeInsets.all(16),
      decoration: const BoxDecoration(
        border: Border(left: BorderSide(color: Colors.black12)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Tasks & Logs",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),

          const SizedBox(height: 20),

          const TaskCard(title: "Task 1.1 Generate Plan", status: "Completed"),

          const TaskCard(
            title: "Task 1.2 Create AKS Cluster",
            status: "Running",
          ),

          const TaskCard(
            title: "Task 1.3 Generate Documentation",
            status: "Pending",
          ),

          const SizedBox(height: 20),

          const Divider(),

          const SizedBox(height: 20),

          const Text(
            "Execution Logs",
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 18),
          ),

          const SizedBox(height: 10),

          const Text("✓ Planner Agent Started"),
          const SizedBox(height: 6),

          const Text("✓ Plan Generated"),
          const SizedBox(height: 6),

          const Text("⚙ AKS Deployment Running"),
          const SizedBox(height: 6),

          const Text("⌛ Waiting Documentation Agent"),
        ],
      ),
    );
  }
}
