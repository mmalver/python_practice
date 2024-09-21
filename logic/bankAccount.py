# you are eligible if you are over 18 and have 500 or more dollars to deposit.

age = int(input("How old are you: "))
depositAmount = int(input("How much do you have to deposit?"))

if age > 18 and depositAmount >= 500:
    print("You are eligible to open an account.")
else:
    print("You do not meet the minimum requirements for opeing an acount")