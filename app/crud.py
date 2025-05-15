from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(**course.model_dump())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def enroll_student(db: Session, enrollment: schemas.EnrollmentCreate):
    # Prevent duplicate enrollments
    existing_enrollment = db.query(models.Enrollment).filter_by(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    ).first()

    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Student is already enrolled in this course")

    db_enroll = models.Enrollment(**enrollment.model_dump())
    db.add(db_enroll)
    db.commit()
    db.refresh(db_enroll)
    return db_enroll

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def get_students(db: Session, skip=0, limit=10):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_courses(db: Session, skip=0, limit=10):
    return db.query(models.Course).offset(skip).limit(limit).all()
