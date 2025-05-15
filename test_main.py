import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import Student, Course, Enrollment

@pytest.fixture(scope="module")
def client():
    return TestClient(app)

@pytest.fixture(scope="function")
def db_session():
    db = SessionLocal()
    yield db
    db.rollback()
    db.close()

def clear_test_data(db_session):
    db_session.query(Enrollment).delete()
    db_session.query(Student).delete()
    db_session.query(Course).delete()
    db_session.commit()

def test_create_student(client, db_session):
    clear_test_data(db_session)
    response = client.post("/students/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "alice@example.com"

def test_enroll_student(client, db_session):
    clear_test_data(db_session)
    student = Student(name="Alice", email="alice@example.com")
    course = Course(title="Math 101", description="Basic Math")
    db_session.add_all([student, course])
    db_session.commit()

    response = client.post("/enroll/", json={"student_id": student.id, "course_id": course.id})
    assert response.status_code == 200
    assert response.json()["student_id"] == student.id
