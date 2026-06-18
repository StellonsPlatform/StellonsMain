from backend.models.infrastructure_intent import (
    InfrastructureIntent,
)

from backend.models.policy_result import (
    PolicyResult,
)

from backend.models.policy_profile import (
    PolicyProfile,
)


class PolicyEngine:

    def __init__(self):

        self.profiles = {

            "startup": PolicyProfile(
                name="startup",
                max_nodes=20,
                max_clusters=2,
                approved_regions=[],
                monitoring_required=False,
                premium_required=False,
            ),

            "enterprise": PolicyProfile(
                name="enterprise",
                max_nodes=100,
                max_clusters=10,
                approved_regions=[],
                monitoring_required=True,
                premium_required=False,
            ),

            "regulated": PolicyProfile(
                name="regulated",
                max_nodes=50,
                max_clusters=5,
                approved_regions=[
                    "East US",
                    "West US",
                    "Central India",
                    "India Central",
                ],
                monitoring_required=True,
                premium_required=True,
            ),
        }

    def evaluate(
        self,
        intent: InfrastructureIntent,
        profile_name: str = "startup",
    ) -> PolicyResult:

        profile = self.profiles.get(
            profile_name,
            self.profiles["startup"],
        )

        violations = []

        warnings = []

        #
        # Production Minimum Nodes
        #

        if (
            intent.environment.lower()
            == "production"
            and intent.node_count < 3
        ):

            violations.append(
                "Production requires at least 3 nodes"
            )

        #
        # Profile Node Limit
        #

        if (
            intent.node_count
            > profile.max_nodes
        ):

            violations.append(
                f"Node count exceeds {profile.name} profile limit"
            )

        #
        # Profile Cluster Limit
        #

        if (
            intent.cluster_count
            > profile.max_clusters
        ):

            violations.append(
                f"Cluster count exceeds {profile.name} profile limit"
            )

        #
        # Monitoring Requirement
        #

        if (
            profile.monitoring_required
            and not intent.monitoring
        ):

            violations.append(
                "Monitoring is required by profile"
            )

        #
        # Premium Requirement
        #

        if (
            profile.premium_required
            and intent.sku_tier.lower()
            != "premium"
        ):

            violations.append(
                "Premium tier is required by profile"
            )

        #
        # Region Restriction
        #

        if (
            len(profile.approved_regions) > 0
            and intent.region
            not in profile.approved_regions
        ):

            violations.append(
                "Region is not approved by profile"
            )

        #
        # Cost Warning
        #

        if intent.node_count >= 20:

            warnings.append(
                "Large deployment detected"
            )

        #
        # Premium Warning
        #

        if (
            intent.sku_tier.lower()
            == "premium"
            and intent.cluster_count > 2
        ):

            warnings.append(
                "Premium multi-cluster deployment may incur high cost"
            )

        return PolicyResult(
            approved=len(violations) == 0,
            violations=violations,
            warnings=warnings,
        )