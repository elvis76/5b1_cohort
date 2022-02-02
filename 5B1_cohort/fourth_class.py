# Dictonary
# my_dict = {"Key":"This is the value", "Key2":"This is another key"}

# # my_Dict = dict()

# a ={"key7":"This is the value", "key5":"This is another key"} #to add a new element to a dictionary

# my_dict.update(a)#to update the dictionary and add mutilpe keys
# print(my_dict)
# print(my_dict.keys()) to add only de keys
# print(my_dict.values())to add only de values
# print(my_dict.items())#to put it in a tuples list

# b = [('Key', 'This is the value'), ('Key2', 'This is another key'), ('key7', 'This is the new value'), ('key5', 'This is another key')]

# print(dict(b))

# popped = my_dict.pop("key7")
# print(popped)
# print(my_dict)

# print(my_dict("key2")) #if u are looking for a specific key
# print(my_dict.get("xyz", "not found"))

# data = {"name":"chuks", "location":"Aba", "job":"Senior frontend", "salary":"$50,000"}

# data["city"] = data.pop("location")

# print(data)

# if "ada" == "john":
#     print("correct")
# else:
#     print("incorrect")


# user_data = {"elvis567.com":"elvis duru"}

# user_email = input("Enter your email:\n>").lower()

# if user_email.isspace() or user_email == "":
#     print("no Entry")
# else:    

#     if user_email in user_data.keys():
#         print("Account already exists")

#     else:
#         choice = input("Do you want to subsribe?(Y/y or N/n)\n>").lower()


#         if choice == 'y':
#             name = input("Enter your full name:\n>")
#             user_data[user_email] = name
#             print("successfully subsricbe")

#         elif choice == 'n':
#             print("Goodbye!")  
#         else:
#             print("invalid input")
# print(user_data)        

#BANK APP vl
# from asyncore import loop
# import sys, string
# punc = string.punctuation
# detail = ()
# bal = 0
# data = {
#     "22367890365": {
#         "name":"Elvis",
#         "dob": "09-09-09",
#         "bvn":"123456789",
#         "pin":"1234",
#         "bal":0
#     },
#      "3927758475" : {
#         "name":"Ife",
#         "dob": "09-09-79",
#         "bvn": "123416789",
#         "pin": "1214",
#         "bal" : 12000
#     },
# }

# print("Welcome to the Astrobank App")
# print("Enter s to signup or l to login or e to exist")
# choice = input(">").lower()

# if choice == 'l':
#     acc_num = input("Enter your account num:\n>")
#     pin = input("Enter your pin:\n>")

#     print(acc_num," ",pin)

#     user = data.get(acc_num)

#     if user and user['pin'] == pin:
#         print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
#     else:
#         print("Invalid Login")