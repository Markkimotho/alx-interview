#!/usr/bin/env python3
"""Module that performs utf-8 text validation
"""


def validUTF8(data):
    """Function that determines if a given
       data set represents a valid UTF-8 encoding.
    """
    num_bytes = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if num & 0b11000000 == 0b10000000:
            # If there are no bytes to continue, it's an invalid encoding
            if num_bytes == 0:
                return False
            # Decrease the count of remaining bytes to continue
            num_bytes -= 1
        else:
            # Get the number of bytes to continue based on the first byte
            if num & 0b11110000 == 0b11110000:
                num_bytes = 3
            elif num & 0b11100000 == 0b11100000:
                num_bytes = 2
            elif num & 0b11000000 == 0b11000000:
                num_bytes = 1
            elif num & 0b10000000 == 0b10000000:
                # If a continuation byte appears without a
                # leading byte, it's invalid
                return False

    # If there are remaining bytes to continue, it's an invalid encoding
    return num_bytes == 0
