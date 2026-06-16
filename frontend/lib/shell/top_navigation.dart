import 'package:flutter/material.dart';

class TopNavigation extends StatelessWidget {
  final VoidCallback onGenerateTemplate;
  final VoidCallback onSaveWorkflow;
  final VoidCallback onLoadWorkflow;

  const TopNavigation({
    super.key,
    required this.onGenerateTemplate,
    required this.onSaveWorkflow,
    required this.onLoadWorkflow,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      height: 72,
      padding: const EdgeInsets.symmetric(horizontal: 24),
      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border(bottom: BorderSide(color: Color(0xFFE5E7EB))),
      ),
      child: Row(
        children: [
          // ==========================================
          // LOGO
          // ==========================================
          const Icon(Icons.hub, size: 30, color: Color(0xFF6F42C1)),

          const SizedBox(width: 12),

          const Text(
            "Stellons",
            style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
          ),

          const SizedBox(width: 12),

          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: const Color(0xFFF3F4F6),
              borderRadius: BorderRadius.circular(8),
            ),
            child: const Text(
              "Cloud Architecture Designer",
              style: TextStyle(fontSize: 12, color: Colors.black87),
            ),
          ),

          const Spacer(),

          // ==========================================
          // GENERATE TEMPLATE
          // ==========================================
          ElevatedButton.icon(
            onPressed: onGenerateTemplate,
            icon: const Icon(Icons.auto_awesome),
            label: const Text("Generate Template"),
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF6F42C1),
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(10),
              ),
            ),
          ),

          const SizedBox(width: 8),

          // ==========================================
          // SAVE WORKFLOW
          // ==========================================
          OutlinedButton.icon(
            onPressed: onSaveWorkflow,
            icon: const Icon(Icons.save_outlined),
            label: const Text("Save"),
          ),

          const SizedBox(width: 8),

          // ==========================================
          // LOAD WORKFLOW
          // ==========================================
          OutlinedButton.icon(
            onPressed: onLoadWorkflow,
            icon: const Icon(Icons.folder_open),
            label: const Text("Load"),
          ),

          const SizedBox(width: 8),

          // ==========================================
          // SHARE
          // ==========================================
          OutlinedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.share),
            label: const Text("Share"),
          ),

          const SizedBox(width: 8),

          // ==========================================
          // NOTIFICATIONS
          // ==========================================
          IconButton(
            onPressed: () {},
            icon: const Icon(Icons.notifications_none),
          ),

          // ==========================================
          // MORE
          // ==========================================
          IconButton(onPressed: () {}, icon: const Icon(Icons.more_horiz)),
        ],
      ),
    );
  }
}
