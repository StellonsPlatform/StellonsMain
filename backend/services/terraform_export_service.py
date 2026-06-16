from pathlib import Path

from backend.models.export_result import (
    ExportResult,
)

from backend.models.terraform_package import (
    TerraformPackage,
)


class TerraformExportService:

    def export(
        self,
        package: TerraformPackage,
        output_dir: str = "generated",
    ) -> ExportResult:

        directory = Path(output_dir)

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        for filename, content in (
            package.files.items()
        ):

            file_path = (
                directory / filename
            )

            file_path.write_text(
                content,
                encoding="utf-8",
            )

        return ExportResult(
            success=True,
            export_path=str(
                directory.resolve()
            ),
            file_count=len(
                package.files
            ),
        )