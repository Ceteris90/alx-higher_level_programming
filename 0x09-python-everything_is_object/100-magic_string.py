#!/usr/bin/python3
from counter import Counter
c = Counter()
def magic_string(): return ", ".join(["Holberton" for i in range(c.inc())])
