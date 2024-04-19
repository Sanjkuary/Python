# #WAF to print the elements of a list in a single line.(list is the parameter)

hero = ["thor", "ironman", "captain america", "shaktiman"]

def print_list(list):
    for item in list:
        print(item, end = " ")


print_list(hero)
print()


cities = ("Delhi", "Noida", "Gurugram", "Mumbai", "pune", "Chennai")

def print_tuple(tpl):
    for item in tpl:
        print(item, end = " ")

print_tuple(cities)
print()
