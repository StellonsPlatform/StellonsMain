import 'dart:convert';

import 'package:http/http.dart' as http;

import '../models/workflow_response.dart';

class ApiService {
  static const String baseUrl = "http://127.0.0.1:8000";

  Future<WorkflowResponse> executeGoal(String goal) async {
    final response = await http.post(
      Uri.parse("$baseUrl/execute"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({"goal": goal}),
    );

    if (response.statusCode != 200) {
      throw Exception("Failed to execute workflow");
    }

    final data = jsonDecode(response.body);

    return WorkflowResponse.fromJson(data);
  }
}
