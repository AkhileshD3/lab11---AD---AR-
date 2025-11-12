"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(num):
    try:
        if num < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(num)
    except ValueError as e:
        print(f"Error: {e}")
        raise
def hypot(num1, num2):
    try:
        return math.hypot(num1, num2)
    except Exception as e:
        print(f"Error Calculating Hypotent: {e}")
        raise
# First example
def add(a, b):
    return a + b
    pass
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError ("Cannot divide by zero")
    return a / b
def log(a,b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid inputs")
    return math.log(b,a)
def exp(a, b):
    return a ** b


