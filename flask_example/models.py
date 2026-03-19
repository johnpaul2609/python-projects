#CRUD OPERATION
from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def get_all_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()
    return data

def add_student(name, email, course):
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO students(name, email, course) VALUES (%s,%s,%s)",
                (name, email, course))
    mysql.connection.commit()
    cur.close()

def get_student(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    data = cur.fetchone()
    cur.close()
    return data

def update_student(id, name, email, course):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE students SET name=%s,email=%s,course=%s WHERE id=%s",
                (name, email, course, id))
    mysql.connection.commit()
    cur.close()

def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()