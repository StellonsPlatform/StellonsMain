import 'package:flutter/material.dart';

import '../workflow/connector_port.dart';

class WorkflowNodeWidget extends StatelessWidget {
  final String title;
  final String subtitle;

  final bool isSelected;

  final VoidCallback onTap;

  final VoidCallback onInputPortTap;
  final VoidCallback onOutputPortTap;

  const WorkflowNodeWidget({
    super.key,
    required this.title,
    required this.subtitle,
    required this.isSelected,
    required this.onTap,
    required this.onInputPortTap,
    required this.onOutputPortTap,
  });

  IconData getNodeIcon() {
    switch (title) {
      case "Planner":
      case "Planner Agent":
        return Icons.auto_awesome;

      case "Azure":
      case "Azure Agent":
        return Icons.cloud;

      case "AWS":
        return Icons.cloud_queue;

      case "AKS Cluster":
        return Icons.hub;

      case "Virtual Network":
        return Icons.device_hub;

      case "Storage Account":
        return Icons.storage;

      case "Database":
        return Icons.dataset;

      case "Monitoring":
        return Icons.monitor_heart;

      case "Key Vault":
        return Icons.lock;

      case "Resource Group":
        return Icons.folder_copy;

      default:
        return Icons.widgets;
    }
  }

  Color getNodeColor() {
    switch (title) {
      case "AKS Cluster":
        return Colors.blue;

      case "Virtual Network":
        return Colors.green;

      case "Database":
        return Colors.orange;

      case "Storage Account":
        return Colors.teal;

      case "Monitoring":
        return Colors.red;

      case "Key Vault":
        return Colors.purple;

      default:
        return const Color(0xFF6F42C1);
    }
  }

  @override
  Widget build(BuildContext context) {
    final nodeColor = getNodeColor();

    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        width: 280,
        height: 140,
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(18),
          border: Border.all(
            color: isSelected ? nodeColor : Colors.grey.shade300,
            width: isSelected ? 3 : 1.5,
          ),
          boxShadow: [
            BoxShadow(
              blurRadius: isSelected ? 20 : 10,
              spreadRadius: isSelected ? 2 : 0,
              color: nodeColor.withAlpha(isSelected ? 60 : 20),
            ),
          ],
        ),
        child: Stack(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Container(
                      width: 42,
                      height: 42,
                      decoration: BoxDecoration(
                        color: nodeColor.withAlpha(30),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Icon(getNodeIcon(), color: nodeColor),
                    ),

                    const SizedBox(width: 12),

                    Expanded(
                      child: Text(
                        title,
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ),

                const SizedBox(height: 14),

                Text(
                  subtitle,
                  style: TextStyle(color: Colors.grey.shade700, fontSize: 14),
                ),

                const SizedBox(height: 14),

                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 5,
                  ),
                  decoration: BoxDecoration(
                    color: nodeColor.withAlpha(20),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  child: Text(
                    title,
                    style: TextStyle(
                      color: nodeColor,
                      fontWeight: FontWeight.w600,
                      fontSize: 11,
                    ),
                  ),
                ),
              ],
            ),

            Positioned(
              left: -9,
              top: 58,
              child: ConnectorPort(color: nodeColor, onTap: onInputPortTap),
            ),

            Positioned(
              right: -9,
              top: 58,
              child: ConnectorPort(color: nodeColor, onTap: onOutputPortTap),
            ),
          ],
        ),
      ),
    );
  }
}
