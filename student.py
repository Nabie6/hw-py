class Student:
    def __init__(self,name,age,major,courses,scores):
        self.name=name
        self.age=age
        self.major=major
        self.courses=courses
        self.scores=scores
       
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I study {self.major}.")

    def major1 (self):
        print(f"My major is {self.major}")

    def gpa1 (self):
        total = sum(self.scores.values())
        self.gpa = total / len(self.scores)
        print(f"My gpa is {self.gpa}")

    def course (self):
        print(f"My courses is {self.courses}")

    def add_course(self, course2,score):
        self.courses.append(course2)
        self.scores[course2]=score
        print(f"It is your full courses {self.courses}")
        
    def update_gpa(self):
        total=sum(self.scores.values())
        self.new_gpa = total / len(self.scores)
        print(f"It is your new gpa: {self.new_gpa}")

    def is_honor(self):
        if self.new_gpa>3.5:
            print("Красный диплом")
        else:
            print("Нет красного диплома")



stud1=Student("Aida",20,"Comaputor Science",  ["Math", "Music","IT"],{"Math": 4.5, "Music": 5.0, "IT": 4.5})

#stud1.introduce()
stud1.major1()
stud1.gpa1()
stud1.course()
stud1.add_course("English",3.5)
stud1.update_gpa()
#stud1.is_honor()
