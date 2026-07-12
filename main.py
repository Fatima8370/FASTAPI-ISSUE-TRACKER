from fastapi import FastAPI # import class
app = FastAPI() 

# variable initialized as the web application
# acts like a controller


"""
items = [
{"id":1, "name": "One"},
{"id":2, "name": "Two"},
{"id":3, "name": "Three"}
]

# get requests
@app.get("/health") # health route
def health_check():
    return {"hello": "Hello World"} # returning json

@app.get("/items") # itmes route
def get_items():
    return items

@app.get("/items/{item_id}")
def get_itemid(item_id: int):
    for item in items:
        if item["id"] == item_id: return item
    return {"error": "Item not found"}

# post requests
@app.post("/items")
def create_items(item: dict):
    items.append(item)
    return item

"""

@app.get("/")
def display ():
    return {"hello": "World"}


# linking routes with the main application
# 
from app.routes.issues import router as issues_router
app.include_router(issues_router)




