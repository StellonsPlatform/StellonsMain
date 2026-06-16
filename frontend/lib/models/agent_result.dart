class AgentResult {
  final String task;
  final String agent;
  final String result;

  AgentResult({required this.task, required this.agent, required this.result});

  factory AgentResult.fromJson(Map<String, dynamic> json) {
    return AgentResult(
      task: json["task"] ?? "",
      agent: json["agent"] ?? "",
      result: json["result"] ?? "",
    );
  }
}
