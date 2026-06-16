import 'agent_result.dart';
import 'task_assignment.dart';

class WorkflowResponse {
  final String goal;

  final List<TaskAssignment> tasks;

  final List<AgentResult> results;

  WorkflowResponse({
    required this.goal,
    required this.tasks,
    required this.results,
  });

  factory WorkflowResponse.fromJson(Map<String, dynamic> json) {
    return WorkflowResponse(
      goal: json["goal"] ?? "",
      tasks: (json["tasks"] as List)
          .map((e) => TaskAssignment.fromJson(e))
          .toList(),
      results: (json["results"] as List)
          .map((e) => AgentResult.fromJson(e))
          .toList(),
    );
  }
}
