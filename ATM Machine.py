import sys

print('Register account')
username= input('Enter username: ')
password= input('Enter Password: ')
print('-------------------------')
print('Login account')
user_name= input("Enter your username: ")
if user_name == username:
    pass1=print("Enter your password: ",end="")
else:
    print('Wrong Input')
    sys.exit()
user_pass= input()
if user_pass==password:
    print("Successfully Login")
else:
    print('Wrong Input')
    sys.exit()

print('-------------------------')
balance = 0

while True:
    print("Welcome to ATM machine")
    print("   [A] Balance \n   [B] Deposit \n   [C] Withdraw \n   [QUIT] Quit")
    picking = input("   Choose: ")
    if picking == 'quit' or picking =='QUIT':
        sys.exit()
    elif picking == 'a' or picking =='A':
        print('Balance: ', balance)
        input('Go back to main menu')
    elif picking == 'b' or picking =='B':
        add_money = int(input('Deposit: '))
        balance = balance+add_money
        input('Go back to main menu')
    elif picking == 'c' or picking =='C':
        minus_money = int(input('Withdraw amount: '))
        if balance<minus_money:
            print('You have insufficient balance')
        else:
            balance = balance-minus_money
        input('Go back to main menu')
    else:
        print('Wrong input')
        break



