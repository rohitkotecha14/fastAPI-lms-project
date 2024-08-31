from typing import List, Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

users = []


class User(BaseModel):
    username: str
    email: str
    is_active: bool
    bio: Optional[str] = None


@router.get("/users", response_model=List[User])
async def get_user():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": users[id]}
