from backend.orchestrator.agent_router import AgentRouter

router = AgentRouter()

tasks = [
    "Create FastAPI endpoint",
    "Create AKS Terraform",
    "Debug Kubernetes CrashLoopBackOff",
    "Design Azure Architecture",
    "Create README"
]

for task in tasks:

    agent = router.route(task)

    print(
        f"{task} -> {type(agent).__name__}"
    )