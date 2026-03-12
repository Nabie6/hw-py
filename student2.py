class Student:
    def __init__(self,name,id,major,courses,gredes):
        self.name=name
        self.id=id
        self.major=major
        self.courses=courses
        self.gredes=gredes


    def add_grade(self,grade):
        self.gredes.append(grade)

    def calculate_average(self):
       avrg=sum(self.gredes)/len(self.gredes)
       print(f"your avarage grade: {avrg}")

    def get_best_grade(self):
        max_grade=max(self.gredes)
        print(f"Best grade: {max_grade}")

    def get_worst_grade(self):
        min_grade=min(self.gredes)
        print(f"Worst grade: {min_grade}")

    def display_info(self): 
        print(f"Student name: {self.name}")
        print(f"Student ID: {self.id}")
        print (f"Student major: {self.major}") 
        print(f" Student courses: {self.courses}")
        print(f"Student score: {self.gredes}")

students = Student({
   "name":["Ali","Sasha","Polina"],
    "id":[101,]
    "major": ["Data science","Data science","Data science"],
    "courses":["It","data dase"]85, 90, 78
    
    })

students.add_grade(95)

students.display_info()

print("Average grade:", students.calculate_average())
print("Best grade:", students.get_best_grade())
print("Worst grade:", students.get_worst_grade())