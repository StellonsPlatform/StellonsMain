class TaskAssignment {
  final String task;
  final String agent;

  TaskAssignment({required this.task, required this.agent});

  factory TaskAssignment.fromJson(Map<String, dynamic> json) {
    return TaskAssignment(task: json["task"] ?? "", agent: json["agent"] ?? "");
  }
}
