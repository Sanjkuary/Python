#using loop function
# for i in range(1, 6):
#     print(i, end = " ")


#using recursion function

# def show(n):
#     if (n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)



# def show(n):
#     if (n == -1):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(5)


# def fact(n):
#     if (n == 0 or n == 1):
#         return 1
#     return fact (n - 1)* n
# print(fact(5)) 

# W A Recursion function to claculate the sum of first n natural number

'''def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n - 1) + n
sum = calc_sum(5)
print(sum)'''

# w A Recursion function to print all elements in a list (use list and index as paramenters)

def print_list(list, idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["Mango", "Lichi", "Apple", "Banana"]

print_list(fruits)