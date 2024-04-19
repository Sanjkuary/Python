# class Student:
#     def __init__(self, name):
#         self.name = name
    
# s1 = Student("Sanjeev")
# print(s1.name)

# del s1.name
# print(s1.name)


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("123456", "abcde")
# print(acc1.acc_no)
# print(acc1.reset_pass())

# class Car: #single inheritance
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car Started.")
    
#     @staticmethod
#     def stop():
#         print("Car Stoped.")

# class Toytacar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = Toytacar("fortuner")
# car2 = Toytacar("puish")

# print(car1.name)
# print(car1.start())
# print(car1.color)

# class Car: #Multi level inheritance
#     color = "Black"
#     @staticmethod
#     def start():
#         print("Car Started.")
    
#     @staticmethod
#     def stop():
#         print("Car Stoped.")

# class Toytacar(Car):
#     def __init__(self,brand):
#         self.brand = brand


# class Fortuner(Toytacar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()

# class A: #Multiple inheritance
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


# class Car: #super method
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car Started.")
    
#     @staticmethod
#     def stop():
#         print("Car Stoped.")

# class Toytacar(Car):
#     def __init__(self,name, type):
#         self.name = name
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = Toytacar("fortuner", "Electric")
# print(car1.type)



# class Person: #classmethod
#     name = "Anonoymous"
#     @classmethod
#     def changeName(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changeName("Sanjeev Kumar")
# print(p1.name)
# print(Person.name)


# class Student: #property decorator
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# stu1 = Student(98,99,97)
# print(stu1.percentage)


