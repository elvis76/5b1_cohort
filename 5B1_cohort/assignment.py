print("Welcome to the Astrobank App")
print("Enter s to signup or l to login or e to exist or d to deposit or w to withdraw")
choice = input(">").lower()
accounts = {}
menu_choice = 0
balance = {}
balance = 0
while True:
    menu_choice = int(input("Type in a number (1-6): "))
    if menu_choice == '1':
        print("sign up")
        name = input("Enter your full name:\n>")
        dob = input("Enter your dob:\n>")
        bvn = input("Enter your bvb:\n>")
        u_pin = input("Create your pin:\n>")

# elif choice == 'e':
#     print('Thank you for banking with us')
#     sys.exit()
# else:
#     print('Wrong choice')
    elif menu_choice == 2:
        print ("Enter a new Accountnumber")
        number = input("New accountnumber: ")
        #phone = input("Number: ")
        accounts[number]=balance
    elif menu_choice == 4:
        print ("Withdraw money from Account.")
        number = input("Accoutnnumber: ")
        if number in accounts:
            withdraw = float(input("How much money would you like to withdraw? > "))
            if withdraw < balance:
                # accounts[number]=balance
                number[balance] -= withdraw
                print (f"Your new balance is ${balance['bal']}")
            else:
                print ("There are no sufficient funds on this accountnumber")
    elif menu_choice == 5:
        print ("Deposit money onto Account.")
        number = input("Accountnumber: ")
        if number in accounts:
            deposit = float(input("How much money would you like to deposit? > "))
            # accounts[number]=balance
            balance += deposit
            print (f"Your new balance is ${balance['bal']}")
        else:
            print ("That accountnumber does not exist.")
    elif menu_choice == 6:
        print("Quit.")
        break
    else:
        print ("Please enter a number between 1 and 6.")