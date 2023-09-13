#!/usr/bin/python3
"""
Minimum number of operations in a text file
Given a text file has a single character "H"
and the operations that can be done in that file are
COPY ALL and PASTE. Find the minimum number of operations
to get n number of characters in the file.

Example:
n = 9
H
COPY ALL -> HH (2 operations)
PASTE -> HHH (1 operation) (Total 3 operations)
COPY ALL -> HHH -> PASTE -> HHHHHH (2 operations) (Total 5 operations)
PASTE -> HHHHHHHHH (1 operation) (Total 6 operations)

Output: 6

Function:
def minOperations(n):
    # your code here
    return 0
"""


def primeNumber(x):
    """
    Function to determine whether number is prime or not
    """
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False


def minOperations(n):
    """
    Function to find the minimum number of operations
    """
    mo = 0
    if n > 1:
        # For prime numbers
        if primeNumber(n):
            for _ in range(1, n):
                mo += 1
            return mo + 1
        # For non-prime numbers
        else:
            for i in range(2, n):
                if n % i == 0:
                    mo += i
                    return mo + minOperations(int(n/i))
    else:
        return 0
