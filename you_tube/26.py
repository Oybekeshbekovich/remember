#CLASS VARIABLES
class Student:
    class_year = 2025
    num_students=0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1=Student("John",20)
student2=Student("Mayk",24)
student3=Student("Tony",32)
student4=Student("Albert",19)
print(f'My graduating class of {Student.class_year} is {Student.num_students} students.')
print(f'Student name is {student1.name}')
print(f'Student name is {student2.name}')
print(f'Student name is {student3.name}')
print(f'Student name is {student4.name}')
