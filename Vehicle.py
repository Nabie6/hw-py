class Vehicle:
    def __init__ (self, brand, model, year):
        self.brand=brand
        self.model=model
        self.year=year
    
    def display_info(self):
        print (f"{self.brand} {self.model} ({self.year})")

class Car(Vehicle):
    def __init__(self,brand, model, year,num_doors):
        super().__init__(brand, model, year)
        self.num_doors=num_doors
    
    def display_info(self):
        super().display_info()
        print (f" Количество дверей: {self.num_doors}")

class Motorcycle (Vehicle):
    def __init__(self,brand, model, year,has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar=has_sidecar
    
    def display_info(self):
        super().display_info()
        print (f" Коляска : {self.has_sidecar}")
    
c1=Car("Toyota", "Camry" , "2022", 4) 
c1.display_info()

m1=Motorcycle("Harley Davidson","Sportster","2020","Отсутствует")
m1.display_info()