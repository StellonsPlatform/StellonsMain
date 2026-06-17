from pydantic import BaseModel


class ExportResult(BaseModel):

    success: bool

    export_path: str

    file_count: int