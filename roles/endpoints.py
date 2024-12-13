from fastapi import APIRouter, Depends, HTTPException
from auth.dependencies import get_current_user_role
from auth.utils import validate_scopes
from roles.services import create_role, fetch_all_roles

router = APIRouter()

@router.get("/")
def get_roles(user=Depends(get_current_user_role)):
    validate_scopes(user["scopes"], ["view_roles"])
    return fetch_all_roles()

@router.post("/")
def create_new_role(
    role_data: dict, user=Depends(get_current_user_role)
):
    if not user["can_create_roles"]:
        raise HTTPException(status_code=403, detail="Not authorized to create roles.")
    validate_scopes(user["scopes"], ["manage_roles"])
    return create_role(role_data)
