# # BANK APP vl
# from asyncore import loop
# import sys, string
# punc = string.punctuation
# detail = ()
# bal = 0
# import random


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

#         print(""":\n what would you like to do?
#              press 1 to withdraw
#              press 2 to deposit
#              press any other to quit.""")
        
#         user_input = input(">")

#         if user_input == "1":
#             amount = int(input("how much?:\n"))
#             if amount >= user['bal']:
#                 print("insufficient funds")
#             else:
#                 user['bal']-= amount
#                 print("take your cash")
#                 print(f"balance is {user['bal']}")
#         elif user_input == "2":
#              amount = int(input("how much?:\n"))

#              user['bal']+= amount
#              print("successfully")
#              print(f"balance is {user['bal']}")
#         else:
#             print("Goodbye")
#     else:
#         print('invalid input')


# elif choice == 's':
#      name = input("Enter your full name:\n>")
#      dob = input("Enter your dob:\n>")
#      bvn = input("Enter your bvn:\n>")
#      pin = input("Create your pin:\n>")
#      details = [('name', name),
#                ('dob', dob),
#                ('bvn', bvn),
#                ('pin', pin),
#                ('bal', 0),
#             ]
     
#      num = [1,2,3,4,5,6,7,8,9,0]
#      acc_num_list = [str(random.choice(num)) for _ in range(10)]

#      acc_num = "".join(acc_num_list)

#      data[acc_num] = dict(details)

# else:
#     print('invalid input')
#     print(data)


# print(random.shuffle(num))
# print(random.sample(num,4))
# print(random.choice(num))
# print(num)

# num = [1,2,3,4,5,6,7,8,9,0]
# random.shuffle(num)
# # com_choice = random.choice(num)
# # print(com_choice)

# trial = 3
# score = 0


# # for i in range(100000000000000):
# #     if trial == 0:
# #         print("Game over")
# #         print(f"your score is {score}")
# #         break
# while trial != 0:

#     choice = random.choice(num)
#     print(choice)
#     user = int(input("pick a number:\n"))

#     if choice == user:
#         trial +=1
#         score +=3
#         print('you won')
#         print("you have been given a extra trial")
#         print("yayyy 😎😎")
#     else:
#         trial -=1
#         print('try again')
#         print(f"you have {trial} trials left")
#         print("Game over")
#         print(f"your score is {score}")
        # break
    
#     # print(choice)
# while True:
#     user_choice = input("Enter a choice (rock, paper, scissors):\n")

#     game_choice = ["rock", "paper", "scissors"]
#     computer_choice = random.choice(game_choice)
#     print(f"\nYou choose {user_choice}, computer choose {computer_choice}:\n")

#     if user_choice == computer_choice:
#         print(f"Both players selected {user_choice}. It's a draw")

#     elif user_choice == "rock":
#         if computer_choice == "scissors":
#             print("Rock smashes scissors You won")
#         else:
#             print("Paper covers rock You lose.")
#     elif user_choice == "paper":
#         if computer_choice == "rock":
#             print("Paper covers rock You won")
#         else:
#             print("Scissors cuts paper You lose.")
#     elif user_choice == "scissors":
#         if computer_choice == "paper":
#             print("Scissors cuts paper You won")
#         else:
#             print("Rock smashes scissors You lose.")

#     play_again = input("Play again? (y/n):\n")
#     if play_again.lower() != "y":
#         print("Game over")
#         break   