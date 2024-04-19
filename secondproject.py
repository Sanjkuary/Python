#Random password generator

import random
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

#list comprehension [Function for i in rnage(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])

password = " "
for i in range(pass_len):
    password += random.choice(charValues)

print("Your password is: ", password)

