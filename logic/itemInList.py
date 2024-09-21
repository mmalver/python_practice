# checks to see if a number is in a list

numbers = range(1,101)
value = int(input("Enter a number to see if it in the list: "))

if value in numbers:
    print("The valie is in the list.")
else:
    print("The item is not in the list.")

words = ["Apple","banana","cherry"]
word = input("Enter a word to see if it is in the list: ")

if word in words:
    print("The item is in the list.")
else:
    print("The item is not in the list.")