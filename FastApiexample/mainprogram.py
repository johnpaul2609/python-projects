from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Employee

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create Employee
@app.post("/employees")
def create_employee(name: str, email: str, department: str, db: Session = Depends(get_db)):
    new_emp = Employee(name=name, email=email, department=department)
    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp

# ✅ Read All Employees
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

# ✅ Read One Employee
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

# ✅ Update Employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, name: str, email: str, department: str, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.name = name
    emp.email = email
    emp.department = department
    db.commit()
    db.refresh(emp)
    return emp

# ✅ Delete Employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully"}