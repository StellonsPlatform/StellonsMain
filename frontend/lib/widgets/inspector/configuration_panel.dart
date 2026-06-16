import 'package:flutter/material.dart';

class ConfigurationPanel extends StatelessWidget {
  const ConfigurationPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 350,

      decoration: BoxDecoration(
        color: Colors.white,
        border: Border(left: BorderSide(color: Colors.grey.shade300)),
      ),

      child: Padding(
        padding: const EdgeInsets.all(20),

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,

          children: [
            const Text(
              "Configuration",
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
            ),

            const SizedBox(height: 24),

            const Text("AKS Cluster"),

            const SizedBox(height: 16),

            TextField(
              decoration: InputDecoration(
                labelText: "Region",
                border: OutlineInputBorder(),
              ),
              controller: TextEditingController(text: "East US"),
            ),

            const SizedBox(height: 16),

            TextField(
              decoration: InputDecoration(
                labelText: "Node Count",
                border: OutlineInputBorder(),
              ),
              controller: TextEditingController(text: "3"),
            ),

            const SizedBox(height: 16),

            TextField(
              decoration: InputDecoration(
                labelText: "VM Size",
                border: OutlineInputBorder(),
              ),
              controller: TextEditingController(text: "Standard_D2s_v3"),
            ),
          ],
        ),
      ),
    );
  }
}
