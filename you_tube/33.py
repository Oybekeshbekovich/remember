#Class methods->ro'yxatdagi hisob kitob uchun
class Student:
    count = 0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    #Instance method
    def get_info(self):
        return f"{self.name} gpa: {self.gpa}"
    @classmethod
    def get_count(cls):
        return f"Total of # student {cls.count}"
    @classmethod
    def get_average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return (f"Average gpa:{cls.total_gpa/cls.count:.2f}")

student1=Student("Jamshid",3.2)
student2=Student("Alisher",2.0)
student3=Student("Abbos",4.1)
print(Student.get_count())
print(Student.get_average_gpa())
