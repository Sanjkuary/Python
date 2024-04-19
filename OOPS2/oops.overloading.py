# #using dunder function

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real, "i +", self.img, "j")

    
#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal,newImg)
    

#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal,newImg)
    
# num1 = Complex(1, 3)
# num1.showNumber()

# num2 = Complex(4, 6)
# num2.showNumber()

# num3 = num1 - num2
# num3.showNumber()


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return(22/7) * self.radius **2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())



# class Employee:
#     def __init__(self,role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role =", self.role)
#         print("dept =", self.dept)
#         print("salary =", self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "75,000")

# # e1 = Employee("Accountant", "Finance", "60000")
# # e1.showDetails()

# engg1 = Engineer("Sanjeev Kumar", 30)
# engg1.showDetails()


class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price
    
# ord1 = Order("chips", 20)
# ord2 = Order("Tea", 15)

# print(ord1 > ord2)

ord1 = Order("Potato", 30)
ord2 = Order("veg", 40)

print(ord1 > ord2)