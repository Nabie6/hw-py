import csv
import os

FILE_NAME = "students.csv"

def save_student(student):
    file_empty = not os.path.exists(FILE_NAME) or os.stat(FILE_NAME).st_size == 0
    
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if file_empty:
            writer.writerow(["ID", "Name", "Age", "Grade", "Email"])
        writer.writerow([student.student_id, student.name, student.age, student.grade, student.email])

def read_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def delete_student(student_id):
    if not os.path.exists(FILE_NAME):
        return
    
    rows = []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    

    new_rows = [rows[0]] + [r for r in rows[1:] if r[0] != str(student_id)]
    
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(new_rows)