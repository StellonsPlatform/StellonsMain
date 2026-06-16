import '../models/workflow_edge.dart';
import '../models/workflow_graph.dart';
import '../models/workflow_node.dart';

class WorkflowGenerator {
  static WorkflowGraph generateAKSWorkflow() {
    final planner = WorkflowNode(
      id: "planner",
      title: "Planner Agent",
      subtitle: "Generate Plan",
      x: 250,
      y: 150,
      config: {"model": "Gemma 3", "temperature": 0.7},
    );

    final azure = WorkflowNode(
      id: "azure",
      title: "Azure Agent",
      subtitle: "Provision AKS",
      x: 700,
      y: 150,
      config: {
        "subscription": "Production",
        "region": "East US",
        "nodeCount": 3,
      },
    );

    final aks = WorkflowNode(
      id: "aks",
      title: "AKS Cluster",
      subtitle: "East US / 3 Nodes",
      x: 1150,
      y: 150,
      config: {"clusterName": "aks-prod", "version": "1.31"},
    );

    return WorkflowGraph(
      nodes: [planner, azure, aks],
      edges: [
        WorkflowEdge(sourceId: "planner", targetId: "azure"),
        WorkflowEdge(sourceId: "azure", targetId: "aks"),
      ],
    );
  }
}
