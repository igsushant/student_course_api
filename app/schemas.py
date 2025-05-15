from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase): pass

class StudentOut(StudentBase):
    id: int

    model_config = {"from_attributes": True}

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase): pass

class CourseOut(CourseBase):
    id: int

    model_config = {"from_attributes": True}

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int

class EnrollmentOut(BaseModel):
    student_id: int
    course_id: int
    enrolled_on: Optional[datetime] = None

    model_config = {"from_attributes": True}

class StudentWithCourses(StudentOut):
    enrollments: List[EnrollmentOut]

class CourseWithStudents(CourseOut):
    enrollments: List[EnrollmentOut]
