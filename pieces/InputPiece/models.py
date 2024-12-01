from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Sleep Piece Input Model
    """

    search: str = Field(
        default="",
        description="Input",
    )


class OutputModel(BaseModel):
    """
    Sleep Piece Output Model
    """
    message: str = Field(
        description="Sleep piece executed"
    )
