# from base64 import standard_b64decode
# import random
# from statistics import median, variance
# import time

# print ("Welcome to RPS")
# print("""\nRules of the game:
# You are expected to choose between R or P or S.
# R for Rock
# P for Rock 
# S for scissors

# Rock trumps Scissors
# Paper trumps Rock
# Scissors trumps Paper""")

# choices = ['r', 'p', 's']
# score = 0
# trial =3

# while trial >0:
#     com_choice = random.choice(choices)
#     print(com_choice)
#     player_choice = input("Choose:\n:").lower()

#     if player_choice not in choices:
#         print("invalid entry")
#         trial -=1
#         print(f"{trial} trial(s) left")

#     else:
#         if player_choice == 'r' and com_choice == 'p':
#             print(f"computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trial(s) left")

#         elif player_choice == 'p' and com_choice == 's':
#             print(f"computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trial(s) left")   

#         elif player_choice == 's' and com_choice == 'r':
#             print(f"computer selected {com_choice.upper()}\nYou lose.")
#             trial -=1
#             print(f"{trial} trial(s) left") 



#         elif com_choice == 'r' and player_choice == 'p':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trial(s) left")  

#         elif com_choice == 'p' and player_choice == 's':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trial(s) left")   

#         elif com_choice == 's' and player_choice == 'r':
#             print("You win")
#             score +=2
#             trial +=1
#             print(f"{trial} trial(s) left")    

#         else:
#             print(" it's a draw")    
#             trial -=1
#             print(f"{trial} trial(s) left")


# print(f"/nYour high score is {score}")
# print("Game over")            

# user_input =input("Enter your number seperated by comma\n>")
# num = [int(i) for i in user_input.split(",")]  # using list of comprehension

# # alternatively, we can use mapping to map a function to the list

# # num =list(map(lambda x : int(x),user_input.split(",")))
# # print(num)
# # print(user_input.split(","))

# # calculating the mean
# mean = sum(num)/len(num)

# # calculating the median
# num.sort()

# midpoint = len(num)//2
# # print(midpoint)
# if len(num)%2 ==0:
#     median = (num[midpoint] + num[midpoint-1])/2
# else:
#     median = num[midpoint]


# #calculating the mode
# freq = {}
# for i in num:
#     freq[i] = freq.get(i,0) +1
# # print(freq)
# mode = max(freq, key=lambda x:freq[x])    
# # print(mode)

# #standard deviation

# standard_deviation = (sum([(x-mean)**2 for x in num])/len(num))**0.5

# #variance
# print("calculating.........\n")
# time.sleep(5)
# print("View results below")

# variance = standard_deviation**2

# print(f"the mean is {round(mean, 2)}")
# print(f"the mean is {median}")
# print(f"the mode is {mode}")
# print(f"the standard deviation is {round(standard_deviation, 2)}")
# print(f"the variance is {round(variance, 2)}")

# print(list(zip([1,2,3,4,5], [1,4,9,16,25])))
# print(dict(zip([1,2,3,4,5], [1,4,9,16,25])))

# user_data = float(input('Enter the principle amount: '))
# time = float(input('Enter the time: '))
# rate = float(input('Enter the rate: '))
# simple_interest = (user_data*time*rate)/100
# print("Simple interest is:", simple_interest)