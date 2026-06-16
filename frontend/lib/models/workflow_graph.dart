import 'workflow_node.dart';
import 'workflow_edge.dart';

class WorkflowGraph {
  List<WorkflowNode> nodes;
  List<WorkflowEdge> edges;

  WorkflowGraph({required this.nodes, required this.edges});

  Map<String, dynamic> toJson() {
    return {
      'nodes': nodes.map((e) => e.toJson()).toList(),
      'edges': edges.map((e) => e.toJson()).toList(),
    };
  }

  factory WorkflowGraph.fromJson(Map<String, dynamic> json) {
    return WorkflowGraph(
      nodes: (json['nodes'] as List)
          .map((e) => WorkflowNode.fromJson(e))
          .toList(),

      edges: (json['edges'] as List)
          .map((e) => WorkflowEdge.fromJson(e))
          .toList(),
    );
  }
}
