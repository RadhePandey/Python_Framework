# a={
#     "first_name" : "Radhe",
#     "last_name"  : "Pandey",
#     "age"  : 28
# }
# print(a)
# print(a["first_name"])

# #Exercise 1: Basic Dictionary Operations

# a["first_name"]="Kaushal"
# a["last_name"]="Singh"
# a["age"]=32
# print(a)


# #Exercise 2: Dictionary Operations

# a["age"]=34   #update age
# print(a,"Update age")



# # Exercise 3: Dictionary from Two Lists

# # Exercise 3: Dictionary from Two Lists
# print("Exercise 3\n")
# keys = ["first_name", "last_name", "age"]
# values = ["Radhe", "Pandey", 28]

# a = {}

# a["first_name"] = "Radhe"
# a["last_name"] = "Pandey"
# a["age"] = 28

# print(a)
# # # Exercise 4: Clear Dictionary

# # a.clear()
# # print(a,"Clear")

# # Exercise 5: Merge Dictionaries

# a = {
#     "first_name": "Radhe",
#     "last_name": "Pandey"
# }

# b = {
#     "age": 28,
#     "city": "Delhi"
# }

# a.update(b)

# print("Merged :", a)


# Exercise 6: Access Nested Dictionary

print("Exercise 6\n")
a = {
    "first_name": "Radhe",
    "last_name": "Pandey",
    "b": 
    {
        "age": 28,
        "city": "Delhi"
    }
}

print(a,"complete dictionary\n")
print("Age:", a["b"]["age"])

# Exercise 7: Access ‘history’ Key From a Nested Dictionary

print("Exercise 7\n")
#here we access age and city 
print("Age:", a["b"]["age"])
print("City:", a["b"]["city"])





# Exercise 8: Initialize Dictionary with Default Values




# Exercise 9: Rename a Key of Dictionary
# Exercise 10: Delete a List of Keys