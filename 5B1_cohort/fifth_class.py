# # BANK APP vl
# from asyncore import loop
# import sys, string
# punc = string.punctuation
# detail = ()
# bal = 0
# import random


# data = {}
# trans_data = {}

# print("Welcome to the AstroBank App")
# while True:
#     print("Enter s to signup or l to login:")
#     print("Enter any other key to close")
#     choice = input(">").lower()

#     if choice == 'l':
#         acc_num = input("Enter your account num:\n>")
#         pin = input("Enter your pin:\n>")

#         user = data.get(acc_num)

#         if user and user['pin'] == pin:
#             print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")

#             while True:
#                 print("""\nWhat would you like to do?
#                     Press 1 to withdraw
#                     Press 2 to deposit
#                     Press 3 to transfer
#                     Press any other key to quit.""")

#                 user_input = input(">")

#                 if user_input == '1':
#                     amount = int(input("How much?\n>"))
#                     if amount >= user['bal']:
#                         print("Insufficient Funds")
#                     else:
#                         user['bal']-=amount

#                         #log transaction data
#                         detail = {
#                             "amount":amount,
#                             "type": "debit",
#                             "action" : "withdrawal"
#                         }

#                         trans_data[acc_num].append(detail)


#                         print("Please take your cash")
#                         print(f"Balance is {user['bal']}")

#                 elif user_input == '2':
#                     amount = int(input("How much?\n>"))

#                     user['bal']+=amount

#                     #log transaction data
#                     detail = {
#                         "amount":amount,
#                         "type": "credit",
#                         "action" : "deposit"
#                     }

#                     trans_data[acc_num].append(detail)

#                     print("Successful")
#                     print(f"Balance is {user['bal']}")
#                 elif user_input == '3':
#                     recepient_ = input("Enter recepient account\n>")
#                     amount = int(input("How much?\n>"))

#                     if user['bal'] < amount:
#                         print("Insufficient Funds")

#                     recepient = data.get(recepient_)
#                     if recepient:
#                         recepient['bal'] += amount
#                         user['bal'] -=amount

#                         #log transaction data
#                         detail = {
#                             "amount":amount,
#                             "type": "debit",
#                             "action" : "transfer"
#                         }

#                         trans_data[acc_num].append(detail)

#                         detail_recepient = {
#                             "amount":amount,
#                             "type": "credit",
#                             "action" : "transfer"
#                         }

#                         trans_data[recepient_].append(detail_recepient)

#                         print("Successful")
#                         print(f"Balance is {user['bal']}")
#                     else:
#                         print(f"Unable to fetch customer with account {recepient_}")

#                 else:
#                     print("Good bye")
#                     break
#         else:
#             print("Invalid Login")

#     elif choice == 's':
#         name = input("Enter your name:\n>")
#         dob= input("Enter your date of birth:\n>")
#         bvn= input("Enter your BVN:\n>")
#         pin = input("Enter your PIN:\n>")
#         details = [('name', name), 
#                 ('dob', dob), 
#                 ('bvn', bvn), 
#                 ('pin', pin), 
#                 ('bal',0) 
#                 ]

#         #generate account number
#         num = [1,2,3,4,5,6,7,8,9,0]
#         acc_num_list = ["3"]
#         acc_num_list.extend([str(random.choice(num)) for _ in range(9)])


#         acc_num = "".join(acc_num_list)

#         data[acc_num] = dict(details)
#         trans_data[acc_num] = []

#         print(f"\nYour account has been created. You account number is {acc_num}\n")

#     else:
#         break



# print(data)
# print(trans_data) 


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
#         print("yayyy ????????")
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