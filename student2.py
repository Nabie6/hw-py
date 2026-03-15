class Student:
    def __init__(self,name,id,major,courses,grades):
        self.name=name
        self.id=id
        self.major=major
        self.courses=courses
        self.grades=grades


    def add_grade(self,grade):
        self.grades.append(grade)

    def calculate_average(self):
       return sum(self.grades)/len(self.grades)
       

    def get_best_grade(self):
        return max(self.grades)
        

    def get_worst_grade(self):
        return min(self.grades)
        

    def display_info(self): 
        print(f"Student name: {self.name}")
        print(f"Student ID: {self.id}")
        print (f"Student major: {self.major}") 
        print(f" Student courses: {self.courses}")
        print(f"Student score: {self.grades}")

class StudentManager:
    def __init__ (self):
        self.students=[]

    def add_student(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()
    def get_top_student(self):
        top_student = self.students[0]

        for student in self.students:
            if student.calculate_average() > top_student.calculate_average():
                top_student = student

        return top_student
    def get_lowest_student(self):
        worst_student = self.students[0]

        for student in self.students:
            if student.calculate_average() < worst_student.calculate_average():
                worst_student = student

        return worst_student

manager = StudentManager()
student1=Student("Ali",101,"Data science",["It","Data Base"],[85, 91])
student2=Student("Sezim",102,"Music",["Gitar","Vocal"],[77, 87])
student3=Student("Aya",103,"Teacher",["History","Kyrgyz language"],[95, 98])


manager.add_student(student1)
manager.add_student(student2)
manager.add_student(student3)

student1.add_grade(95)
student2.add_grade(90)
student3.add_grade(85)

manager.display_all_students()
print()
print("Лучший студент:")
top_student = manager.get_top_student()
top_student.display_info()
print()
print("Студент с худшими оценками:")
worst_student = manager.get_lowest_student()
worst_student.display_info()
print()

for student in manager.students:
    student.display_info()
    print("Average grade:", student.calculate_average())
    print("Best grade:", student.get_best_grade())
    print("Worst grade:", student.get_worst_grade())
    print()
