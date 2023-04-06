#!/usr/bin/python3
def magic_string():
    class Counter: i = 0; def inc(cls): cls.i += 1; return cls.i
    return ", ".join(["Holberton" for i in range(Counter.inc())])
