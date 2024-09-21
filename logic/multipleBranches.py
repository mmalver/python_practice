# amusement park admision
# under 4 is free
# under 18 is 20
# over 18 is 60

age = int(input("What is your age:"))

if age > 18:
    print("Your admission price is $60.00")
elif age > 4:
    print("Your admission price is $20.00")
else:
    print("Your admission price is free.")