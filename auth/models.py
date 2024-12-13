from pydantic import BaseModel

class Role(BaseModel):
    name: str
    can_create_roles: bool
    scopes: list[str]
