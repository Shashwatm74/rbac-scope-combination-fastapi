from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user_role
from auth.utils import validate_scopes
from submissions.services import get_all_submissions, create_submission

router = APIRouter()

@router.get("/")
def list_submissions(user=Depends(get_current_user_role)):
    validate_scopes(user["scopes"], ["view_submissions"])
    return get_all_submissions()

@router.post("/")
def new_submission(submission: dict, user=Depends(get_current_user_role)):
    validate_scopes(user["scopes"], ["submit_tasks"])
    return create_submission(submission, user["name"])
