#!/usr/bin/python3
"""
Module with function to calculate square units of water retained after it rains
"""


def rain(walls):
    """
    Function to calculate the volume of water stored between walls

    walls: (list) list of non-negative integers

    returns: (int) indicating total amount of rainwater collected
    """
    volume = 0
    if not walls or len(walls) < 3:
        return 0
    volume = 0
    for i in range(1, len(walls) - 1):
        left = max(walls[:i])
        right = max(walls[i + 1:])
        if walls[i] < left and walls[i] < right:
            volume += min(left, right) - walls[i]
    return volume
