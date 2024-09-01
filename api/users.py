from typing import List, Optional

import fastapi
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.utils.courses import get_user_courses
from api.utils.users import *
from db.config import get_db
from schemas.course import Course
from schemas.user import User

router = APIRouter()


@router.get("/users", response_model=List[User])
async def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user is not None:
        raise HTTPException(status_code=400, detail="Email is already registered")

    return create_user(db=db, user=user)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user


@router.get("/users/{user_id}/courses", response_model=List[Course])
async def read_courses(user_id: int, db: Session = Depends(get_db)):
    courses = get_user_courses(db, user_id)
    return courses

