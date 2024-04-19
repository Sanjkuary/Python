# class Student:
#     name = "Sanjeev"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "Blue"
#     brand = "Toyota"
# car1 = Car()
# print(car1.color)
# print(car1.brand)



# class Student:
#     college_name = "ABC College"
#     def __init__(self, name):
#         self.name = name
#         print("adding new student in databses..")

# s1 = Student("Sanjeev")
# print(s1.name)

# s2 = Student("Arjun")
# print(s2.name)


# class Student:
#     college_name = "ABC College"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in databses..")

# s1 = Student("Sanjeev", 88)
# print(s1.name, s1.marks)
# print(s1.college_name)

# s2 = Student("Arjun", 94)
# print(s2.name, s2.marks)



# class Student:
#     @staticmethod
#     def hello():
#         print("Hello")

# s1.hello()




class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")

car1 = Car()
car1.start()
