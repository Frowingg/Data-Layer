from pydantic import BaseModel

class response(BaseModel):
    message: str
    result: object | None = None