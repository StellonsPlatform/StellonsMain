import 'dart:convert';
import 'dart:html' as html;

import '../models/workflow_edge.dart';
import '../models/workflow_graph.dart';
import '../models/workflow_node.dart';

class WorkflowStorageService {
  static const String storageKey = "stellons_workflow";

  // =====================================================
  // EXPORT GRAPH TO JSON
  // =====================================================

  static String exportGraph(WorkflowGraph graph) {
    final workflow = {
      "nodes": graph.nodes
          .map(
            (node) => {
              "id": node.id,
              "title": node.title,
              "subtitle": node.subtitle,
              "x": node.x,
              "y": node.y,
              "config": node.config,
            },
          )
          .toList(),
      "edges": graph.edges
          .map((edge) => {"sourceId": edge.sourceId, "targetId": edge.targetId})
          .toList(),
    };

    return const JsonEncoder.withIndent("  ").convert(workflow);
  }

  // =====================================================
  // IMPORT GRAPH FROM JSON
  // =====================================================

  static WorkflowGraph importGraph(String jsonString) {
    final data = jsonDecode(jsonString);

    final nodes = (data["nodes"] as List)
        .map(
          (node) => WorkflowNode(
            id: node["id"],
            title: node["title"],
            subtitle: node["subtitle"],
            x: (node["x"] as num).toDouble(),
            y: (node["y"] as num).toDouble(),
            config: Map<String, dynamic>.from(node["config"]),
          ),
        )
        .toList();

    final edges = (data["edges"] as List)
        .map(
          (edge) => WorkflowEdge(
            sourceId: edge["sourceId"],
            targetId: edge["targetId"],
          ),
        )
        .toList();

    return WorkflowGraph(nodes: nodes, edges: edges);
  }

  // =====================================================
  // SAVE TO BROWSER LOCAL STORAGE
  // =====================================================

  static void saveGraph(WorkflowGraph graph) {
    final json = exportGraph(graph);

    html.window.localStorage[storageKey] = json;
  }

  // =====================================================
  // LOAD FROM BROWSER LOCAL STORAGE
  // =====================================================

  static WorkflowGraph? loadGraph() {
    final json = html.window.localStorage[storageKey];

    if (json == null || json.isEmpty) {
      return null;
    }

    return importGraph(json);
  }

  // =====================================================
  // DELETE SAVED WORKFLOW
  // =====================================================

  static void clearGraph() {
    html.window.localStorage.remove(storageKey);
  }
}
