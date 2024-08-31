from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title= "FastAPI Project",
    description="FastAPI Project",
    version="0.1.0",
    contact={
        "name": "Rohit Kotecha",
        "email": "rohit.kotecha@sjsu.edu",
    }
)


users = []


class User(BaseModel):
    username: str
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/users", response_model=List[User])
async def get_user():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
        id: int = Path(..., description="User's ID", gt=2),
        is_active: str = Query(None, description="User's status", max_length=5),
):
    return {"user": users[id], "is_active": is_active}
