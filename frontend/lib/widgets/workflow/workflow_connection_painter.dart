import 'package:flutter/material.dart';

import '../../models/workflow_edge.dart';
import '../../models/workflow_node.dart';

class WorkflowConnectionPainter extends CustomPainter {
  final List<WorkflowNode> nodes;
  final List<WorkflowEdge> edges;

  WorkflowConnectionPainter({required this.nodes, required this.edges});

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.deepPurple
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;

    for (final edge in edges) {
      final source = nodes.firstWhere((n) => n.id == edge.sourceId);

      final target = nodes.firstWhere((n) => n.id == edge.targetId);

      final start = Offset(source.x + 220, source.y + 50);

      final end = Offset(target.x, target.y + 50);

      canvas.drawLine(start, end, paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return true;
  }
}
