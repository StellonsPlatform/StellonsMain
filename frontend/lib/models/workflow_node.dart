class WorkflowNode {
  String id;
  String title;
  String subtitle;

  double x;
  double y;

  Map<String, dynamic> config;

  WorkflowNode({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.x,
    required this.y,
    required this.config,
  });

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'title': title,
      'subtitle': subtitle,
      'x': x,
      'y': y,
      'config': config,
    };
  }

  factory WorkflowNode.fromJson(Map<String, dynamic> json) {
    return WorkflowNode(
      id: json['id'],
      title: json['title'],
      subtitle: json['subtitle'],
      x: (json['x'] as num).toDouble(),
      y: (json['y'] as num).toDouble(),
      config: Map<String, dynamic>.from(json['config']),
    );
  }
}
