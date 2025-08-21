#Static method-> ro'yxatning ichida bor yo'qligini tekshiradi
class Employee:
    def __init__(self, name,position):
        self.name = name
        self.position = position
    def get_info(self):
        return f"{self.name}={self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['A','B','C','D','E','F']
        return position in valid_positions

employee1 = Employee('James','manager')
employee2 = Employee('Luys','shef')
employee3 = Employee('Jordan','admin')

print(Employee.is_valid_position('A'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())