# Use the Math function to Factorial a number
import math

def factorial(num):

    if num > 0:
        result = num * math.factorial(num - 1)
        return result 
    else:
        return 1