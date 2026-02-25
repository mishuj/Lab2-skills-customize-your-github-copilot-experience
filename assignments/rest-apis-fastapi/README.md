# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework. You'll create endpoints to handle HTTP requests, manage data, and understand the fundamentals of API design and development.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Server

#### Description
Set up a FastAPI application with a basic server that responds to HTTP requests. Create at least two GET endpoints that return data in JSON format.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define at least 2 GET endpoints with different routes
- Return JSON formatted data from the endpoints
- Include appropriate HTTP status codes
- Run successfully on localhost:8000


### 🛠️ Implement CRUD Operations

#### Description
Extend your API to handle Create, Read, Update, and Delete operations on a simple data model. Use in-memory storage (a list or dictionary) to store the data.

#### Requirements
Completed program should:

- Implement POST endpoint to create new items
- Implement GET endpoint(s) to retrieve items (all items and by ID)
- Implement PUT endpoint to update an existing item
- Implement DELETE endpoint to remove an item
- Include proper error handling for invalid requests (e.g., item not found)
- Use appropriate HTTP methods and status codes (200, 201, 204, 404)


### 🛠️ Add Data Validation

#### Description
Use Pydantic models to define the structure of your data and validate incoming requests. This ensures your API only accepts properly formatted data.

#### Requirements
Completed program should:

- Define a Pydantic model for your data structure
- Use the model for request body validation
- Return descriptive error messages for invalid data
- Include at least one optional field with a default value
- Test the validation with both valid and invalid requests

