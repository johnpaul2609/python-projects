import numpy as np

no_students = int(input("Enter number of students: "))
no_semesters = int(input("Enter number of semesters: "))
no_subjects = int(input("Enter number of subjects: "))

p_list = []

for i in range(0, no_students):
    sem_list = []
    for j in range(0, no_semesters):
        marks_list = []
        for k in range(0, no_subjects):
            m = int(input(f"Student: {i + 1} Semester: {j + 1}, Enter mark in subject {k + 1}: "))
            marks_list.append(m)
        sem_list.append(marks_list)
    p_list.append(sem_list)
print(p_list)
print(np.array(p_list))