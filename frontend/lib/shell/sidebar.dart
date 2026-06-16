import 'package:flutter/material.dart';

import '../widgets/sidebar/navigation_menu.dart';
import '../widgets/sidebar/subscription_tree.dart';
import '../widgets/sidebar/profile_card.dart';

class Sidebar extends StatelessWidget {
  const Sidebar({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        color: Color(0xFFF9F9F9),
        border: Border(right: BorderSide(color: Color(0xFFE5E7EB))),
      ),
      child: const Column(
        children: [
          Expanded(
            child: SingleChildScrollView(
              child: Column(
                children: [
                  SizedBox(height: 16),

                  NavigationMenu(),

                  Divider(),

                  SubscriptionTree(),
                ],
              ),
            ),
          ),

          ProfileCard(),
        ],
      ),
    );
  }
}
