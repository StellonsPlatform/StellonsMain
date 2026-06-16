class WorkflowEdge {
  final String sourceId;
  final String targetId;

  WorkflowEdge({required this.sourceId, required this.targetId});

  Map<String, dynamic> toJson() {
    return {'sourceId': sourceId, 'targetId': targetId};
  }

  factory WorkflowEdge.fromJson(Map<String, dynamic> json) {
    return WorkflowEdge(sourceId: json['sourceId'], targetId: json['targetId']);
  }
}
