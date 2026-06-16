import 'package:flutter/material.dart';

class TaskCard extends StatelessWidget {
  final String title;
  final String status;

  const TaskCard({super.key, required this.title, required this.status});

  Color getStatusColor() {
    switch (status) {
      case "Completed":
        return Colors.green;
      case "Running":
        return Colors.orange;
      case "Pending":
        return Colors.grey;
      default:
        return Colors.blue;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(title),
        trailing: Chip(
          backgroundColor: getStatusColor(),
          label: Text(status, style: const TextStyle(color: Colors.white)),
        ),
      ),
    );
  }
}
