from fastapi import FastAPI
from api import users, courses, sections

app = FastAPI(
    title="FastAPI Project",
    description="FastAPI Project",
    version="0.1.0",
    contact={
        "name": "Rohit Kotecha",
        "email": "rohit.kotecha@sjsu.edu",
    }
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
