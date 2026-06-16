from backend.models.terraform_project import (
    TerraformProject,
)

from backend.models.terraform_validation import (
    TerraformValidation,
)


class TerraformValidationService:

    def validate(
        self,
        project: TerraformProject,
    ) -> TerraformValidation:

        errors = []

        warnings = []

        if not project.main_tf.strip():

            errors.append(
                "main.tf is empty"
            )

        if not project.variables_tf.strip():

            errors.append(
                "variables.tf is empty"
            )

        if not project.outputs_tf.strip():

            warnings.append(
                "outputs.tf is empty"
            )

        if "azurerm_kubernetes_cluster" not in (
            project.main_tf
        ):

            errors.append(
                "AKS resource not found"
            )

        if "variable \"environment\"" not in (
            project.variables_tf
        ):

            errors.append(
                "environment variable missing"
            )

        return TerraformValidation(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
        )