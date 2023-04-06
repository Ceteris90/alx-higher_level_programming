#!/usr/bin/python3
def magic_string():
    class Counter: i = 0
    return ", ".join(["Holberton" for i in range(Counter.i := Counter.i + 1)])
