# This program counts from 1 to 20. If a number is divisible by 5, i places the phrase (BING) before the number.

for number in range(1,21,2):
    if (number % 5 == 0):
        print (f"(BING) {number}")
    else:
        print(number)

        