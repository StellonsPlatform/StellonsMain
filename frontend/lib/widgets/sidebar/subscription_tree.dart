import 'package:flutter/material.dart';

class SubscriptionTree extends StatelessWidget {
  const SubscriptionTree({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "CLOUD SUBSCRIPTIONS",
            style: TextStyle(
              fontSize: 11,
              fontWeight: FontWeight.bold,
              color: Colors.grey,
            ),
          ),

          const SizedBox(height: 16),

          ExpansionTile(
            initiallyExpanded: true,
            title: const Text("Subscription 1"),
            subtitle: const Text("Azure"),
            children: [
              ExpansionTile(
                title: const Text("Resource Group"),
                children: [
                  const ListTile(title: Text("US Central")),

                  const ListTile(title: Text("Kubernetes Cluster")),

                  const ListTile(title: Text("CoreDB Instance")),

                  const ListTile(title: Text("Live Orchestrator")),
                ],
              ),
            ],
          ),

          ExpansionTile(
            title: const Text("Subscription 2"),
            subtitle: const Text("AWS"),
            children: const [],
          ),
        ],
      ),
    );
  }
}
