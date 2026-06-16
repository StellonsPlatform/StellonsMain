import 'package:flutter/material.dart';

import '../../models/workflow_node.dart';

class NodeConfigurationPanel extends StatefulWidget {
  final WorkflowNode node;

  const NodeConfigurationPanel({super.key, required this.node});

  @override
  State<NodeConfigurationPanel> createState() => _NodeConfigurationPanelState();
}

class _NodeConfigurationPanelState extends State<NodeConfigurationPanel> {
  int selectedTab = 0;

  final List<String> aksTabs = [
    "Basics",
    "Networking",
    "Scaling",
    "Security",
    "Monitoring",
    "Tags",
    "Review",
  ];

  Widget buildField(String label, String value) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label, style: const TextStyle(fontWeight: FontWeight.w600)),
          const SizedBox(height: 8),
          TextFormField(
            initialValue: value,
            decoration: InputDecoration(
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(10),
              ),
              isDense: true,
            ),
          ),
        ],
      ),
    );
  }

  Widget buildTabMenu() {
    return Container(
      width: 140,
      decoration: const BoxDecoration(
        border: Border(right: BorderSide(color: Color(0xFFE5E7EB))),
      ),
      child: ListView.builder(
        itemCount: aksTabs.length,
        itemBuilder: (context, index) {
          final selected = selectedTab == index;

          return ListTile(
            selected: selected,
            selectedTileColor: Colors.deepPurple.withAlpha(25),
            title: Text(
              aksTabs[index],
              style: TextStyle(
                color: selected ? Colors.deepPurple : Colors.black87,
                fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
              ),
            ),
            onTap: () {
              setState(() {
                selectedTab = index;
              });
            },
          );
        },
      ),
    );
  }

  Widget buildAKSContent() {
    switch (selectedTab) {
      case 0:
        return Column(
          children: [
            buildField("Cluster Name", "aks-prod"),
            buildField("Region", "East US"),
            buildField("Kubernetes Version", "1.31"),
          ],
        );

      case 1:
        return Column(
          children: [
            buildField("Network Plugin", "Azure CNI"),
            buildField("Address Space", "10.0.0.0/16"),
            buildField("Subnet", "10.0.1.0/24"),
          ],
        );

      case 2:
        return Column(
          children: [
            buildField("Node Count", "3"),
            buildField("VM Size", "Standard_D4s_v5"),
            buildField("Autoscaling", "Enabled"),
          ],
        );

      case 3:
        return Column(
          children: [
            buildField("Private Cluster", "False"),
            buildField("Azure RBAC", "Enabled"),
          ],
        );

      case 4:
        return Column(
          children: [
            buildField("Log Analytics", "Enabled"),
            buildField("Container Insights", "Enabled"),
          ],
        );

      case 5:
        return Column(
          children: [
            buildField("Environment", "Production"),
            buildField("Owner", "Platform Team"),
          ],
        );

      case 6:
        return Column(
          children: const [
            ListTile(
              title: Text("Cluster Ready"),
              subtitle: Text("Review configuration before deployment"),
            ),
          ],
        );

      default:
        return const SizedBox();
    }
  }

  Widget buildSimpleResourceForm() {
    switch (widget.node.title) {
      case "Virtual Network":
        return Column(
          children: [
            buildField("Address Space", "10.0.0.0/16"),
            buildField("Subnet", "10.0.1.0/24"),
            buildField("DNS", "Default"),
            buildField("Peering", "Disabled"),
          ],
        );

      case "Storage Account":
        return Column(
          children: [
            buildField("Account Name", "stproduction001"),
            buildField("Performance", "Standard"),
            buildField("Replication", "LRS"),
            buildField("Access Tier", "Hot"),
          ],
        );

      case "Database":
        return Column(
          children: [
            buildField("Engine", "PostgreSQL"),
            buildField("Version", "16"),
            buildField("Storage", "128 GB"),
            buildField("Backup", "7 Days"),
            buildField("High Availability", "Enabled"),
          ],
        );

      case "Monitoring":
        return Column(
          children: [
            buildField("Workspace", "log-analytics"),
            buildField("Retention", "30 Days"),
          ],
        );

      case "Key Vault":
        return Column(
          children: [
            buildField("Vault Name", "kv-production"),
            buildField("SKU", "Standard"),
          ],
        );

      default:
        return Column(
          children: [
            buildField("Name", widget.node.title),
            buildField("Description", widget.node.subtitle),
          ],
        );
    }
  }

  Widget buildContent() {
    if (widget.node.title == "AKS Cluster") {
      return Row(
        children: [
          buildTabMenu(),
          Expanded(
            child: SingleChildScrollView(
              padding: const EdgeInsets.all(20),
              child: buildAKSContent(),
            ),
          ),
        ],
      );
    }

    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: buildSimpleResourceForm(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 420,
      color: Colors.white,
      child: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(20),
            decoration: const BoxDecoration(
              border: Border(bottom: BorderSide(color: Color(0xFFE5E7EB))),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Text(
                    widget.node.title,
                    style: const TextStyle(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                IconButton(onPressed: () {}, icon: const Icon(Icons.close)),
              ],
            ),
          ),

          Expanded(child: buildContent()),

          Container(
            padding: const EdgeInsets.all(20),
            decoration: const BoxDecoration(
              border: Border(top: BorderSide(color: Color(0xFFE5E7EB))),
            ),
            child: SizedBox(
              width: double.infinity,
              height: 50,
              child: ElevatedButton(
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.deepPurple,
                  foregroundColor: Colors.white,
                ),
                child: const Text("Save Configuration"),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
