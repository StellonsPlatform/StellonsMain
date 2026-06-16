import 'package:flutter/material.dart';

class NavigationMenu extends StatelessWidget {
  const NavigationMenu({super.key});

  Widget item(IconData icon, String title) {
    return ListTile(
      dense: true,
      leading: Icon(icon, size: 18, color: Colors.grey),
      title: Text(title, style: const TextStyle(fontSize: 13)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        item(Icons.add, "New Chat"),

        item(Icons.search, "Search Chat"),

        item(Icons.extension, "MCP Plugin"),

        item(Icons.apps, "Other Apps"),

        item(Icons.more_horiz, "More"),
      ],
    );
  }
}
