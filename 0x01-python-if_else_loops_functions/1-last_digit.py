#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

reminder = abs(number) % 10
if number < 0:
    digit = -1*reminder
    if digit == 0:
        print(f"Last digit of {number:d} is {digit:d} and is Zero")
    else:
        print(f"Last digit of {number:d} is {digit:d} and is less than 6 and not 0")
elif reminder > 5:
    print(f"Last digit of {number:d} is {reminder:d} and is greater than 5")
elif reminder == 0:
    print(f"Last digit of {number:d} is {reminder:d} and is zero")
else:
    print(f"Last digit of {number:d} is {reminder:d} and is less than 6 and not 0")
