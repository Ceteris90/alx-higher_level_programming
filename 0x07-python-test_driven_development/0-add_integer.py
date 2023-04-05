#!/usr/bin/python3

def add_integer(a, b=98):
    # Check that both arguments are either integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or a float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or a float")
    
    # Convert the arguments to integers and add them
    try:
        result = int(a) + int(b)
    except ValueError:
        raise ValueError("cannot convert arguments to integers")
    
    # Return the result
    return result
