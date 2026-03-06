import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox, simpledialog

from sqlalchemy import (
    create_engine, Column, Integer, String, Numeric, DateTime, ForeignKey, func
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# -----------------------
# Database configuration
# -----------------------
DB_CONFIG = {
    "USERNAME": "root",
    "PASSWORD": "johnpaul%40123",  # change if needed
    "HOST": "localhost",
    "DATABASE": "testdb1",
    "ECHO": True,
}

DATABASE_URL = f"mysql+pymysql://{DB_CONFIG['USERNAME']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}/{DB_CONFIG['DATABASE']}"

engine = create_engine(DATABASE_URL, echo=DB_CONFIG["ECHO"], pool_pre_ping=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    course = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Student(name={self.name}, email={self.email})>"

Base.metadata.create_all(engine)

def add_student(name, age, email, course):
    try:
        student = Student(
            name=name,
            age=int(age),
            email=email,
            course=course
        )
        session.add(student)
        session.commit()
        messagebox.showinfo("Success", "Student added successfully!")
    except Exception as e:
        session.rollback()
        messagebox.showerror("Error", f"Failed to add student\n{e}")

# add_student(name="john", age=24, email="abc@gmail.com", course="DBMS")
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x300")

# Labels and Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Course").pack()
course_entry = tk.Entry(root)
course_entry.pack()

def submit_student():
    add_student(
        name_entry.get(),
        age_entry.get(),
        email_entry.get(),
        course_entry.get()
    )

tk.Button(root, text="Add Student", command=submit_student).pack(pady=10)

root.mainloop()