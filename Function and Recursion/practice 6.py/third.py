#WAF to find the factorial of n.(n is the parameter)

def calc_fact(n):
    fact = 1
    for i in range (1, n+1):
        fact *= i
    print(fact)

calc_fact(5)
calc_fact(6)
calc_fact(7)
calc_fact(8)
calc_fact(9)