import datetime
x= datetime.datetime.now()
print(x)

cashAvailable = 200000





# login system and register
# login - account_number, 4 digit password,email_address
# sign_up - generate account_number, password, email
# bank operations - withdraw, transfer, deposit,check balance

import random
user_database = {}

def initialize():
    print("***Welcome to Code Bank***")

    init = int(input("Do you have an account with us: \n (1)Yes \n (2) No \n "))
    if init == 1:
        login()
    elif init == 2:
        sign_up()

    else:
        print("You have selected an invalid option")
        init()


def sign_up():
    print("**Sign Up**")
    email = input("what is your email address: \n")
    first_name = input("What is your first name:\n")
    last_name = input("What is your last name: \n")
    pin = int(input("What is your four digit pin: \n"))

    if " " in email or "@" not in email:
        print("There should be no space in your email please try again and there should be an @ symbol")
        sign_up()
    else:
        account_number = acct_number()

        user_database[account_number] = [first_name, last_name, email, pin]

        print("Your account has been created")
        print("=" * 30)
        print("Your account number is : " + str(account_number))
        print("Make sure you keep it safe")
        print("=" * 30)

        login()


def login():
    print("###Login###")

    account_number_from_user = int(input("What is your account number: \n"))
    pin = int(input("Your 4-digit pin:\n"))
    for  accountNumber, userDetails in user_database.items():
        if accountNumber == account_number_from_user:
            if userDetails[3] == pin:
                bank_operations(userDetails)
            else:
                print("Invalid option try again")
                login()


def acct_number():
    return random.randrange(0000000000, 9999999999)

def bank_operations(user):
    print("Welcome %s " % user[0], user[1])
    print("Current Balance: %d " % cashAvailable)

    option = int(input("What would you like to do? (1) deposit \n (2) withdrawal \n (3) Redirect to login \n ("
                       "4)Logout \n  "))

    if option == 1:
        deposit()
    elif option == 2:
        withdrawal()
    elif option == 3:
        login()
    elif option == 4:
        exit()


def withdrawal():
    withdraw = int(input("How much do you want to withdraw \n"))
    if withdraw > cashAvailable:
        print("You can't withdraw up to this amount")

    else:
        print("Take your cash")
        print("your new balance is " + str(cashAvailable-withdraw))

def deposit():
    deposition = int(input("How much would you like to deposit:\n"))
    print("You have deposited " + str(deposition) + "to your account")
    print("Your new balance is " + str(deposition+cashAvailable))


def logout():
    login()


initialize()






