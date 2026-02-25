from fastapi import FastAPI
from pydantic import BaseModel

# Create a FastAPI application instance
app = FastAPI()

# Define a Pydantic model for data validation
class Item(BaseModel):
    id: int
    title: str
    description: str = "No description provided"  # Optional field with default value
    completed: bool = False

# In-memory data storage
items_db = []

# GET endpoint - retrieve all items
@app.get("/items")
def get_all_items():
    """Retrieve all items from the database"""
    return {"items": items_db}


# GET endpoint - retrieve a specific item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a specific item by its ID"""
    for item in items_db:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}, 404


# POST endpoint - create a new item
@app.post("/items", status_code=201)
def create_item(item: Item):
    """Create a new item in the database"""
    item_dict = item.dict()
    items_db.append(item_dict)
    return {"message": "Item created successfully", "item": item_dict}


# PUT endpoint - update an existing item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """Update an existing item"""
    for i, existing_item in enumerate(items_db):
        if existing_item["id"] == item_id:
            items_db[i] = item.dict()
            return {"message": "Item updated successfully", "item": items_db[i]}
    return {"error": "Item not found"}, 404


# DELETE endpoint - remove an item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Delete an item from the database"""
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db.pop(i)
            return
    return {"error": "Item not found"}, 404


# Run the application with: uvicorn starter-code:app --reload
