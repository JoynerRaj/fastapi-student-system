from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from app.database.connection import SessionLocal
from app.database.operations import *
from app.models.student import Student

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
def read_students(request: Request, db: Session = Depends(get_db)):

    students = get_students(db)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "students": students}
    )


@router.post("/students")
def add_student(
    id: int = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    db: Session = Depends(get_db)
):

    student = Student(id=id, name=name, age=age)

    create_student(db, student)

    return RedirectResponse("/", status_code=303)


@router.get("/edit/{student_id}", response_class=HTMLResponse)
def edit_student(student_id: int, request: Request, db: Session = Depends(get_db)):

    student = get_student(db, student_id)

    return templates.TemplateResponse(
        "edit.html",
        {"request": request, "student": student}
    )


@router.post("/update/{student_id}")
def update_student_route(
    student_id: int,
    name: str = Form(...),
    age: int = Form(...),
    db: Session = Depends(get_db)
):

    update_student(db, student_id, name, age)

    return RedirectResponse("/", status_code=303)


@router.post("/delete/{student_id}")
def delete_student_route(student_id: int, db: Session = Depends(get_db)):

    delete_student(db, student_id)

    return RedirectResponse("/", status_code=303)