from pydantic import BaseModel

class ItemIMS(BaseModel):
    formulario : object | None = None
