#cretae student class that takes name and marks of 3 subjects as arguments in constuctor, 
#then cretae a method to print the average.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "Your avg score is:", sum/3)

# s1 = Student("Sanjeev Kumar", [99, 98, 97])
# s1.get_avg()

# s1.name = "ironman"
# s1.get_avg()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         total = sum(self.marks)
#         avg = total / len(self.marks)
#         print("Hi", self.name, "Your avg score is:", avg)

# s1 = Student("Sanjeev Kumar", [99, 98, 97])
# s1.get_avg()

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return(self.balance)
    
# acc1 = Account(10000, 123456)

# acc1.debit(1000)

# acc2 = Account(5000, 105020)
# acc2.debit(500)



acc3 = Account( 4000, 56239)
acc3.debit(1000)
acc3.credit(2000)







