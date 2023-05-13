#!/usr/bin/env python3
def calculate_fibonacci(n):
    """
    This function calculates the nth number in the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
