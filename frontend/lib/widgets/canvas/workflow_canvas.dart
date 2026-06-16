import 'package:flutter/material.dart';

import '../../models/workflow_edge.dart';
import '../../models/workflow_graph.dart';
import '../../models/workflow_node.dart';

import '../../services/template_generator.dart';
import '../../services/workflow_generator.dart';
import '../../services/workflow_storage_service.dart';

import '../workflow/node_configuration_panel.dart';
import '../workflow/node_toolbox.dart';
import '../workflow/prompt_bar.dart';
import '../workflow/workflow_connection_painter.dart';

import 'workflow_node_widget.dart';

class WorkflowCanvas extends StatefulWidget {
  const WorkflowCanvas({super.key});

  @override
  State<WorkflowCanvas> createState() => WorkflowCanvasState();
}

class WorkflowCanvasState extends State<WorkflowCanvas> {
  late WorkflowGraph graph;

  WorkflowNode? selectedNode;

  String? connectionSourceId;

  final TextEditingController promptController = TextEditingController();

  @override
  void initState() {
    super.initState();

    graph = WorkflowGenerator.generateAKSWorkflow();
  }

  @override
  void dispose() {
    promptController.dispose();
    super.dispose();
  }

  // =====================================================
  // GENERATE AKS TEMPLATE
  // =====================================================

  void generateAKSTemplate() {
    setState(() {
      graph = TemplateGenerator.generateAKSTemplate();

      selectedNode = null;

      connectionSourceId = null;
    });

    ScaffoldMessenger.of(
      context,
    ).showSnackBar(const SnackBar(content: Text("AKS Template Generated")));
  }

  // =====================================================
  // PROMPT → ARCHITECTURE
  // =====================================================

  void generateFromPrompt() {
    final prompt = promptController.text.trim().toLowerCase();

    setState(() {
      if (prompt.contains("aks") ||
          prompt.contains("kubernetes") ||
          prompt.contains("cluster")) {
        graph = TemplateGenerator.generateAKSTemplate();
      } else if (prompt.contains("database") ||
          prompt.contains("postgres") ||
          prompt.contains("postgresql") ||
          prompt.contains("mysql")) {
        graph = TemplateGenerator.generateDatabaseTemplate();
      } else if (prompt.contains("storage")) {
        graph = TemplateGenerator.generateStorageTemplate();
      } else if (prompt.contains("vault") ||
          prompt.contains("key vault") ||
          prompt.contains("secret")) {
        graph = TemplateGenerator.generateKeyVaultTemplate();
      }

      selectedNode = null;

      connectionSourceId = null;
    });
  }

  // =====================================================
  // SAVE WORKFLOW
  // =====================================================

  void saveWorkflow() {
    WorkflowStorageService.saveGraph(graph);

    final exportedJson = WorkflowStorageService.exportGraph(graph);

    debugPrint("========================================");

    debugPrint(exportedJson);

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text("Workflow saved to browser storage")),
    );
  }

  // =====================================================
  // LOAD WORKFLOW
  // =====================================================

  void loadWorkflow() {
    final loadedGraph = WorkflowStorageService.loadGraph();

    if (loadedGraph == null) {
      ScaffoldMessenger.of(
        context,
      ).showSnackBar(const SnackBar(content: Text("No saved workflow found")));

      return;
    }

    setState(() {
      graph = loadedGraph;

      selectedNode = null;

      connectionSourceId = null;
    });

    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(content: Text("Workflow loaded successfully")),
    );
  }

  // =====================================================
  // CONNECTIONS
  // =====================================================

  void startConnection(String nodeId) {
    setState(() {
      connectionSourceId = nodeId;
    });

    debugPrint("SOURCE NODE SELECTED: $nodeId");
  }

  void completeConnection(String targetId) {
    if (connectionSourceId == null) {
      return;
    }

    if (connectionSourceId == targetId) {
      return;
    }

    final edgeExists = graph.edges.any(
      (edge) =>
          edge.sourceId == connectionSourceId && edge.targetId == targetId,
    );

    if (edgeExists) {
      return;
    }

    setState(() {
      graph.edges.add(
        WorkflowEdge(sourceId: connectionSourceId!, targetId: targetId),
      );

      connectionSourceId = null;
    });

    debugPrint("EDGE CREATED");
  }

  // =====================================================
  // ADD NODE FROM TOOLBOX
  // =====================================================

  void addNode(String nodeTitle) {
    setState(() {
      graph.nodes.add(
        WorkflowNode(
          id: DateTime.now().millisecondsSinceEpoch.toString(),

          title: nodeTitle,

          subtitle: "New Component",

          x: 500,
          y: 450,

          config: {},
        ),
      );
    });
  }

  // =====================================================
  // UI
  // =====================================================

  @override
  Widget build(BuildContext context) {
    return DragTarget<String>(
      onAcceptWithDetails: (details) {
        addNode(details.data);
      },
      builder: (context, candidateData, rejectedData) {
        return GestureDetector(
          onTap: () {
            setState(() {
              selectedNode = null;
            });
          },
          child: Container(
            color: const Color(0xFFF8F9FB),

            child: Stack(
              children: [
                // ======================================
                // GRID
                // ======================================
                Positioned.fill(child: CustomPaint(painter: GridPainter())),

                // ======================================
                // CONNECTIONS
                // ======================================
                Positioned.fill(
                  child: CustomPaint(
                    painter: WorkflowConnectionPainter(
                      nodes: graph.nodes,
                      edges: graph.edges,
                    ),
                  ),
                ),

                // ======================================
                // PROMPT BAR
                // ======================================
                Positioned(
                  top: 20,
                  left: 250,
                  right: 20,
                  child: PromptBar(
                    controller: promptController,
                    onGenerate: generateFromPrompt,
                  ),
                ),

                // ======================================
                // TOOLBOX
                // ======================================
                const Positioned(left: 20, top: 20, child: NodeToolbox()),

                // ======================================
                // NODES
                // ======================================
                ...graph.nodes.map(
                  (node) => Positioned(
                    left: node.x,
                    top: node.y,
                    child: GestureDetector(
                      onPanUpdate: (details) {
                        setState(() {
                          node.x += details.delta.dx;

                          node.y += details.delta.dy;
                        });
                      },
                      child: WorkflowNodeWidget(
                        title: node.title,

                        subtitle: node.subtitle,

                        isSelected: selectedNode?.id == node.id,

                        onTap: () {
                          setState(() {
                            selectedNode = node;
                          });
                        },

                        onInputPortTap: () {
                          completeConnection(node.id);
                        },

                        onOutputPortTap: () {
                          startConnection(node.id);
                        },
                      ),
                    ),
                  ),
                ),

                // ======================================
                // CONFIGURATION PANEL
                // ======================================
                AnimatedPositioned(
                  duration: const Duration(milliseconds: 300),

                  curve: Curves.easeInOut,

                  top: 0,
                  bottom: 0,

                  right: selectedNode == null ? -360 : 0,

                  child: selectedNode == null
                      ? const SizedBox()
                      : NodeConfigurationPanel(node: selectedNode!),
                ),

                // ======================================
                // SAVE BUTTON
                // ======================================
                Positioned(
                  right: 20,
                  bottom: 20,
                  child: FloatingActionButton.extended(
                    heroTag: "saveWorkflow",

                    onPressed: saveWorkflow,

                    icon: const Icon(Icons.save),

                    label: const Text("Save JSON"),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }
}

// =========================================================
// GRID PAINTER
// =========================================================

class GridPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    const spacing = 25.0;

    final paint = Paint()
      ..color = Colors.grey.withValues(alpha: 0.10)
      ..strokeWidth = 1;

    for (double x = 0; x < size.width; x += spacing) {
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), paint);
    }

    for (double y = 0; y < size.height; y += spacing) {
      canvas.drawLine(Offset(0, y), Offset(size.width, y), paint);
    }
  }

  @override
  bool shouldRepaint(CustomPainter oldDelegate) {
    return false;
  }
}
