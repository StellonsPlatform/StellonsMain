from pydantic import BaseModel


class TerraformProject(BaseModel):

    main_tf: str

    variables_tf: str

    outputs_tf: str

    terraform_tfvars: str