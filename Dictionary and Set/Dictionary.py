info = {
    "key" : "value",
    "name" : "sanjeev kumar", #Srting data type
    "learning" : "coding", # string data type
    "age" : 35, #int data type
    "marks" : 94.5, #folat data type
    "is adult": True, #boolian data type
    "subject": ["python", "C", "java"], #list
    "topic" : ("dict", "set"), # tuple
}
print(info)
print(type(info))
print(info["name"])
print(info["topic"])
print(info["subject"])
print(info["age"])
print(info["is adult"])

info["name"] = "Aryan"
info["suname"] = "yadav"

print(info)
