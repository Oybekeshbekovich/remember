# OOP

# Class
# initilization
# incapsulation
# polimorphizm

class Avotmabil:
    def __init__(self, name, year, kompaniya_name, color):
        self.name = name
        self.year = year
        self.kompaniya_name = kompaniya_name
        self.color = color
        print("Creat car!!")

    def create_avtomabil(self):
        print(
            f"{self.color} rangli {self.name} nomli avtomabil  {self.kompaniya_name} komponiya tomonidan "
            f"{self.year}-yilda yaratildi.")


Avotmabil1 = Avotmabil("M3", 2009, "BMW", "ko'k")
Avotmabil1.create_avtomabil()

# print(Avotmabil1.name)
# print(Avotmabil1.year)
# print(Avotmabil1.kompaniya_name)

class Fly_Car(Avotmabil):
    def __init__(self, name, year, kompaniya_name,qanot ):
        super().__init__(name,year,kompaniya_name)
        self.qanot= qanot
        print("Creat car !!@")

FLY_car1 = Fly_Car("Tesle", 2009, "BMW", "qizil")