from pathlib import Path

from backend.models.terraform_project import (
    TerraformProject,
)

from backend.models.terraform_package import (
    TerraformPackage,
)


class TerraformPackagingService:

    def package(
        self,
        project: TerraformProject,
    ) -> TerraformPackage:

        return TerraformPackage(
            files={
                "main.tf": project.main_tf,
                "variables.tf": project.variables_tf,
                "outputs.tf": project.outputs_tf,
                "terraform.tfvars": project.terraform_tfvars,
            }
        )

    def write(
        self,
        project: TerraformProject,
    ) -> str:

        package = self.package(
            project
        )

        output_dir = Path(
            "generated"
        )

        output_dir.mkdir(
            exist_ok=True
        )

        for (
            filename,
            content,
        ) in package.files.items():

            file_path = (
                output_dir / filename
            )

            file_path.write_text(
                content,
                encoding="utf-8",
            )

        return str(output_dir)