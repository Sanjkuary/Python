#WAP to find the sum of first n numbers. (using for)

# n = int(input("enter number : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total number :", sum)

#WAP to find the sum of first n numbers. (using while)

# n = int(input("enter number : "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("total number: ", sum)

#WAP to find the factorial of first n numbers.(using while)
# n = int(input("enter number :"))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("factorial :", fact)

#WAP to find the factorial of first n numbers.(using for)

n = int(input("enter number :"))
fact = 1
for i in range(1, n+1):
    fact *= i

print("factorial =", fact)