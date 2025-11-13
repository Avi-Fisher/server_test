from pydantic import BaseModel


class Caesar(BaseModel):

    text: str
    offset: int
    mode: str

















