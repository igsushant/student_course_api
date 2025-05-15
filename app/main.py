from fastapi import FastAPI
from app.routers import students, course, enrollments

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollments.router, prefix="/enroll", tags=["Enrollments"])
