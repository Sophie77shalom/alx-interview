#!/usr/bin/python3
""" Task 0"""


def minOperations(n):
    """
    minOperations
    """
    # all outputs should be at least 2  
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # divides by root
        if n % root == 0:
            # total even-divisions  
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root  
            root -= 1
        # increment root  
        root += 1
    return ops
