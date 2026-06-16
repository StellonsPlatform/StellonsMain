from backend.orchestrator.llm_router import LLMRouter


router = LLMRouter()

from backend.orchestrator.llm_router import LLMRouter


router = LLMRouter()


tasks = [
    "Design AKS networking architecture",
    "Create FastAPI backend",
    "Deploy Kubernetes cluster",
    "Write project documentation",
    "Debug container startup failure",
]


for task in tasks:

    result = router.route(task)

    print(
        "\n========================"
    )

    print(
        f"Task: {task}"
    )

    print(
        f"Agent: {result.agent}"
    )

    print(
        f"Confidence: {result.confidence}"
    )

    print(
        f"Reason: {result.reasoning}"
    )
tasks = [
    "Design AKS networking architecture",
    "Create FastAPI backend",
    "Deploy Kubernetes cluster",
    "Write project documentation",
    "Debug container startup failure",
]


for task in tasks:

    result = router.route(task)

    print(
        "\n========================"
    )

    print(
        f"Task: {task}"
    )

    print(
        f"Agent: {result.agent}"
    )

    print(
        f"Confidence: {result.confidence}"
    )

    print(
        f"Reason: {result.reasoning}"
    )