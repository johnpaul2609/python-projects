from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import mysql, init_db, get_all_students, add_student, get_student, update_student, delete_student

app = Flask(__name__)
app.config.from_object(Config)

init_db(app)

# Home Page
@app.route('/')
def index():
    students = get_all_students()
    return render_template('index.html', students=students)

# Add Student
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        add_student(name, email, course)
        return redirect(url_for('index'))
    return render_template('add_student.html')

# Edit Student
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = get_student(id)
    if request.method == 'POST':
        print("edit button clicked")
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        update_student(id, name, email, course)
        return redirect(url_for('index'))
    return render_template('edit_student.html', student=student)

# Delete Student
@app.route('/delete/<int:id>')
def delete(id):
    delete_student(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)