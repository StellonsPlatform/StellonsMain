import 'package:flutter/material.dart';
import '../widgets/workflow/workflow_node_card.dart';

class Workspace extends StatelessWidget {
  const Workspace({super.key});

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(32),
          child: Center(
            child: Container(
              constraints: const BoxConstraints(maxWidth: 900),
              child: Column(
                children: [
                  const Text(
                    "Workflow #001",
                    style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                  ),

                  const SizedBox(height: 12),

                  const Text(
                    "Goal",
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.w600),
                  ),

                  const SizedBox(height: 8),

                  const Text(
                    "Create AKS cluster in East US with 3 nodes",
                    textAlign: TextAlign.center,
                  ),

                  const SizedBox(height: 40),

                  const WorkflowNodeCard(
                    title: "Generate Plan",
                    agent: "Planner Agent",
                    status: "Completed",
                  ),

                  const SizedBox(height: 12),

                  const Icon(Icons.arrow_downward, size: 30),

                  const SizedBox(height: 12),

                  const WorkflowNodeCard(
                    title: "Deploy AKS",
                    agent: "DevOps Agent",
                    status: "Running",
                  ),

                  const SizedBox(height: 12),

                  const Icon(Icons.arrow_downward, size: 30),

                  const SizedBox(height: 12),

                  const WorkflowNodeCard(
                    title: "Generate Documentation",
                    agent: "Documentation Agent",
                    status: "Pending",
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
