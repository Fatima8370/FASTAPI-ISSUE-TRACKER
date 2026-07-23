import uuid
from fastapi import APIRouter 
# class used to group related API routes

router = APIRouter(prefix= "/api/v1/issues", tags=["issues"]) # tags for swagger docs

@router.get("/")
def get_issues():
    return []




