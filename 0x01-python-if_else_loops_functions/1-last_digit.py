#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

reminder = number % 10

if reminder > 5:
    print(f"Last digit of {number:d} is {reminder:d} and is greater than 5")
elif reminder == 0:
    print(f"Last digit of {number:d} is {reminder:d} and is zero")
else:
    print(f"Last digit of {number:d} is {reminder:d} and is less than 6 and not 0")
