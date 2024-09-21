# est to see if a number is even.

def isEven( number):
    return number % 2 == 0

number = int(input("Enter a number: "))
if isEven(number):
    print (f"The number {number} is even.")
else:
    print(f"The number {number} is most ertainly not even")
    