from pydantic import BaseModel


class Resume(BaseModel):
    Resume: str | None
    DataType: str | None
