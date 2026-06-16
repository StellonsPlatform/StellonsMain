class ConnectionStateModel {
  String? sourceNodeId;

  ConnectionStateModel({this.sourceNodeId});

  void clear() {
    sourceNodeId = null;
  }
}
