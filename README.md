# Student Course API

A FastAPI-based backend application to manage Students, Courses, and Enrollments using PostgreSQL or SQLite.

---

## 🚀 Features

- Create and fetch Students and Courses
- Enroll Students in Courses
- Fetch a Student with enrolled Courses
- Fetch a Course with enrolled Students
- Email validation with Pydantic
- Pagination for list responses
- Alembic-based schema migrations
- Unit testing with pytest

---

## 🏗️ Project Structure
student_course_api/
├── alembic/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ └── routers/
│ ├── students.py
│ ├── courses.py
│ └── enrollments.py
├── test_main.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── sample_curls.md

2. Create and Activate a Virtual Environment-

python -m venv .venv
# For Windows:
.venv\Scripts\activate
# For Linux/macOS:
source .venv/bin/activate

3. Install Dependencies-

pip install -r requirements.txt
For development/testing:
pip install -r requirements-dev.txt

4. Configure Database-
### 🔧 PostgreSQL Setup (Optional)

If using PostgreSQL instead of SQLite, you can create your database and user manually via `psql`:

```sql
-- Access psql as postgres or an admin user
CREATE DATABASE database;
CREATE USER username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE database TO username;
```

Create a .env file in the root directory:
DATABASE_URL=sqlite:///./test.db

Or for PostgreSQL:
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database>
(Replace <username>, <password>, and <database> with your actual PostgreSQL values.)

5. Apply Migrations-
alembic upgrade head

6. Run the App-
uvicorn app.main:app --reload

Then Visit:
Swagger Docs: http://127.0.0.1:8000/docs
Redoc: http://127.0.0.1:8000/redoc

Running Tests-
pytest

Bonus Features Implemented
✅ Email validation
✅ Pagination for list responses
✅ Alembic for migrations
✅ Unit testing with pytest

📬 API Testing
See sample_curls.md file or use Swagger UI at /docs

