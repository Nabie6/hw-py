class Student:
    def __init__(self, student_id, name, age, grade, email):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.grade=grade
        self.email=email

    def __str__(self):
        return f"ID: {self.student_id}, name: {self.name},age: {self.age},grade: {self.grade},email: {self.email}"
