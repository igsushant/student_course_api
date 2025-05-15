## ✅ `sample_curls.md`

```markdown
# Sample CURL Commands to Test the API
```
## 📌 Create a Student

```bash
curl -X POST http://127.0.0.1:8000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'
```
## Create a Course
```
curl -X POST http://127.0.0.1:8000/courses/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Math 101", "description": "Introductory Math"}'
```

## Enroll a Student in a Course
```
curl -X POST http://127.0.0.1:8000/enroll/ \
  -H "Content-Type: application/json" \
  -d '{"student_id": 1, "course_id": 1}'
```
## Get Student Details (with enrolled courses)
```
curl http://127.0.0.1:8000/students/1
```
## Get Course Details (with enrolled students)
```
curl http://127.0.0.1:8000/courses/1
```

## Get Paginated List of Students
```
curl "http://127.0.0.1:8000/students/?skip=0&limit=10"
```

## Get Paginated List of Courses
```
curl "http://127.0.0.1:8000/courses/?skip=0&limit=10"
```
