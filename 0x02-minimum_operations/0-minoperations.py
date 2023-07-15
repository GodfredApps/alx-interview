#!/usr/bin/python3
"""
This module contains a function to calculate the fewest number of operations
needed to have exactly `n` H characters in a text file.
"""


def minOperations(n):

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
