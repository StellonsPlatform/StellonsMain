import '../models/workflow_edge.dart';
import '../models/workflow_graph.dart';
import '../models/workflow_node.dart';

class TemplateGenerator {
  // =====================================================
  // AKS TEMPLATE
  // =====================================================

  static WorkflowGraph generateAKSTemplate() {
    final rg = WorkflowNode(
      id: 'rg',
      title: 'Resource Group',
      subtitle: 'Production RG',
      x: 250,
      y: 320,
      config: {'name': 'rg-production', 'region': 'East US'},
    );

    final vnet = WorkflowNode(
      id: 'vnet',
      title: 'Virtual Network',
      subtitle: '10.0.0.0/16',
      x: 650,
      y: 320,
      config: {
        'addressSpace': '10.0.0.0/16',
        'subnet': '10.0.1.0/24',
        'dns': 'Default',
        'peering': 'Disabled',
      },
    );

    final aks = WorkflowNode(
      id: 'aks',
      title: 'AKS Cluster',
      subtitle: 'East US / 3 Nodes',
      x: 1050,
      y: 320,
      config: {
        'clusterName': 'aks-prod',
        'region': 'East US',
        'nodeCount': 3,
        'vmSize': 'Standard_D4s_v5',
        'autoscaling': 'Enabled',
        'kubernetesVersion': '1.31',
      },
    );

    final monitor = WorkflowNode(
      id: 'monitor',
      title: 'Monitoring',
      subtitle: 'Azure Monitor',
      x: 1450,
      y: 320,
      config: {'workspace': 'log-analytics'},
    );

    return WorkflowGraph(
      nodes: [rg, vnet, aks, monitor],
      edges: [
        WorkflowEdge(sourceId: rg.id, targetId: vnet.id),
        WorkflowEdge(sourceId: vnet.id, targetId: aks.id),
        WorkflowEdge(sourceId: aks.id, targetId: monitor.id),
      ],
    );
  }

  // =====================================================
  // DATABASE TEMPLATE
  // =====================================================

  static WorkflowGraph generateDatabaseTemplate() {
    final rg = WorkflowNode(
      id: 'rg',
      title: 'Resource Group',
      subtitle: 'Database RG',
      x: 250,
      y: 320,
      config: {'name': 'rg-database', 'region': 'East US'},
    );

    final db = WorkflowNode(
      id: 'db',
      title: 'Database',
      subtitle: 'PostgreSQL Flexible Server',
      x: 750,
      y: 320,
      config: {
        'engine': 'PostgreSQL',
        'version': '16',
        'storage': '128 GB',
        'backup': '7 Days',
        'highAvailability': 'Enabled',
      },
    );

    final monitor = WorkflowNode(
      id: 'monitor',
      title: 'Monitoring',
      subtitle: 'Azure Monitor',
      x: 1250,
      y: 320,
      config: {'workspace': 'log-analytics'},
    );

    return WorkflowGraph(
      nodes: [rg, db, monitor],
      edges: [
        WorkflowEdge(sourceId: rg.id, targetId: db.id),
        WorkflowEdge(sourceId: db.id, targetId: monitor.id),
      ],
    );
  }

  // =====================================================
  // STORAGE TEMPLATE
  // =====================================================

  static WorkflowGraph generateStorageTemplate() {
    final rg = WorkflowNode(
      id: 'rg',
      title: 'Resource Group',
      subtitle: 'Storage RG',
      x: 250,
      y: 320,
      config: {'name': 'rg-storage', 'region': 'East US'},
    );

    final storage = WorkflowNode(
      id: 'storage',
      title: 'Storage Account',
      subtitle: 'Blob Storage',
      x: 750,
      y: 320,
      config: {
        'accountName': 'stproduction001',
        'performance': 'Standard',
        'replication': 'LRS',
        'accessTier': 'Hot',
      },
    );

    final monitor = WorkflowNode(
      id: 'monitor',
      title: 'Monitoring',
      subtitle: 'Azure Monitor',
      x: 1250,
      y: 320,
      config: {'workspace': 'log-analytics'},
    );

    return WorkflowGraph(
      nodes: [rg, storage, monitor],
      edges: [
        WorkflowEdge(sourceId: rg.id, targetId: storage.id),
        WorkflowEdge(sourceId: storage.id, targetId: monitor.id),
      ],
    );
  }

  // =====================================================
  // KEY VAULT TEMPLATE
  // =====================================================

  static WorkflowGraph generateKeyVaultTemplate() {
    final rg = WorkflowNode(
      id: 'rg',
      title: 'Resource Group',
      subtitle: 'Security RG',
      x: 250,
      y: 320,
      config: {'name': 'rg-security'},
    );

    final vault = WorkflowNode(
      id: 'vault',
      title: 'Key Vault',
      subtitle: 'Secrets Management',
      x: 750,
      y: 320,
      config: {'vaultName': 'kv-production', 'sku': 'Standard'},
    );

    return WorkflowGraph(
      nodes: [rg, vault],
      edges: [WorkflowEdge(sourceId: rg.id, targetId: vault.id)],
    );
  }
}
