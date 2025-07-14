from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory store
memory = {"result": None}


# Request model
class Numbers(BaseModel):
    x: float
    y: float


# POST → ADDITION
@app.post("/add")
def add(numbers: Numbers):
    result = numbers.x + numbers.y
    memory["result"] = result
    return {"operation": "add", "result": result}


# GET → SUBTRACTION (use query parameters)
@app.get("/subtract")
def subtract(x: float, y: float):
    result = x - y
    memory["result"] = result
    return {"operation": "subtract", "result": result}


# PUT → MULTIPLICATION
@app.put("/multiply")
def multiply(numbers: Numbers):
    result = numbers.x * numbers.y
    memory["result"] = result
    return {"operation": "multiply", "result": result}


# DELETE → DIVISION (use query parameters)
@app.delete("/divide")
def divide(x: float, y: float):
    if y == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    result = x / y
    memory["result"] = result
    return {"operation": "divide", "result": result}
