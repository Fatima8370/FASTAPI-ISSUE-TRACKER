import uuid
from fastapi import APIRouter, HTTPException, status
from app.schemas import IssueCreate, IssueOut, IssueUpdate, IssueStatus
from app.storage import load_data, save_data

# class used to group related API routes

router = APIRouter(prefix= "/api/v1/issues", tags=["issues"]) # tags for swagger docs

@router.get("/", response_model=list[IssueOut])
def get_issues():
    '''Retrieve all issues'''
    issues = load_data
    return issues

@router.post("/", response_model= "IssueOut", status_code= status.HTTP_201_CREATED)
def create_issue(issue: IssueCreate):
    '''Create New issue'''
    issues = load_data()
    new_issue = IssueOut(
        id= str (uuid.uuid4()),
        title= issue.title,
        description= issue.description,
        priority= issue.priority,
            status= IssueStatus.open,
    )
    



