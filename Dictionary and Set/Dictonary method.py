student = {
    "name1" : "sanjeev kumar", 
    "name2" : "rahul kumar", 
    "subject" : {
        "phy" : 94.2,
        "chem" : 85.4,
        "math" : 87.6
    }
}

print(student.keys()) #it will show only outer layer keys, not the nested keys.
print(list(student.keys()))
print(len(list(student.keys())))
print(type(student))

print(student.values()) #it will retun all values including nasted values.
print(list(student.values())) #in ths list form and thete is dictionary in the same list.
print(student.items()) # it will show all key, val in touple forms.
print(list(student.items()))
pair = list(student.items())
print(pair[0])

print(student["subject"].get("chem"))

new_dict = {"name3":"Aryan", "city": "Delhi", "age": 16} #we can add or update key values.
student.update(new_dict)
print(student)

print(student["subject"]["chem"])
