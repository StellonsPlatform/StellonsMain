import 'package:flutter/material.dart';

import '../widgets/canvas/workflow_canvas.dart';

import 'sidebar.dart';
import 'top_navigation.dart';

class StellonsShell extends StatefulWidget {
  const StellonsShell({super.key});

  @override
  State<StellonsShell> createState() => _StellonsShellState();
}

class _StellonsShellState extends State<StellonsShell> {
  final GlobalKey<WorkflowCanvasState> workflowCanvasKey =
      GlobalKey<WorkflowCanvasState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,

      body: Row(
        children: [
          // ==========================================
          // SIDEBAR
          // ==========================================
          const SizedBox(width: 240, child: Sidebar()),

          // ==========================================
          // MAIN CONTENT
          // ==========================================
          Expanded(
            child: Column(
              children: [
                TopNavigation(
                  onGenerateTemplate: () {
                    workflowCanvasKey.currentState?.generateAKSTemplate();
                  },

                  onSaveWorkflow: () {
                    workflowCanvasKey.currentState?.saveWorkflow();
                  },

                  onLoadWorkflow: () {
                    workflowCanvasKey.currentState?.loadWorkflow();
                  },
                ),

                Expanded(child: WorkflowCanvas(key: workflowCanvasKey)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
