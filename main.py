from fastapi import FastAPI # import class
from app.routes.issues import router as issues_router   
app = FastAPI() 

# variable initialized as the web application
# acts like a controller

app.include_router(issues_router)

@app.get("/")
def display ():
    return {"hello": "World"}




