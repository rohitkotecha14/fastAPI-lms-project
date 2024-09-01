from typing import List

import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from api.utils.courses import *
from db.config import get_db
from schemas.course import Course

router = fastapi.APIRouter()


@router.get("/courses", response_model=List[Course])
async def read_courses(db: Session = Depends(get_db)):
    courses = get_courses(db=db)
    return courses


@router.post("/courses", response_model=Course, status_code=status.HTTP_201_CREATED)
async def create_new_course(course: CourseCreate, db: Session = Depends(get_db)):
    return create_course(course=course, db=db)


@router.get("/courses/{course_id}", response_model=Course)
async def read_user(course_id: int, db: Session = Depends(get_db)):
    db_course = get_course(db, course_id)

    if db_course is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    return db_course
