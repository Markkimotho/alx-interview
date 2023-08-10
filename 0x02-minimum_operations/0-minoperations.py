#!/usr/bin/python3
"""Module For Minimum Operations
"""


def minOperations(n):
    """Calculates the fewest number of operations...
    needed to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    current_length = 1
    clipboard = 1

    while current_length < n:
        if n % current_length == 0:
            clipboard = current_length
            operations += 1

        current_length += clipboard
        operations += 1

    return operations
