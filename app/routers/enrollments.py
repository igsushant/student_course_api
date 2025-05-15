from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.EnrollmentOut)
def enroll_student(enrollment: schemas.EnrollmentCreate, db: Session = Depends(database.get_db)):
    student = db.get(models.Student, enrollment.student_id)
    course = db.get(models.Course, enrollment.course_id)
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    new_enrollment = models.Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        enrolled_on=datetime.utcnow()
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment
