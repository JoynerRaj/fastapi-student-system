from sqlalchemy.orm import Session
from app.models.student import Student


def get_students(db: Session):
    return db.query(Student).all()


def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def create_student(db: Session, student: Student):

    db.add(student)

    db.commit()

    db.refresh(student)

    return student


def update_student(db: Session, student_id: int, name: str, age: int):

    student = db.query(Student).filter(Student.id == student_id).first()

    student.name = name

    student.age = age

    db.commit()


def delete_student(db: Session, student_id: int):

    student = db.query(Student).filter(Student.id == student_id).first()

    db.delete(student)

    db.commit()