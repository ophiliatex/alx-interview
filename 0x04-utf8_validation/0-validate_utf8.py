#!/usr/bin/python3
"""
The script contains a function to validate UTF-8 encoding
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes.
    :return: Boolean indicating if the data is a valid UTF-8 encoding.
    """

    num_byte = 0

    for byte in data:
        if num_byte == 0:
            if (byte >> 7) == 0:
                continue
            if (byte >> 5) == 0b110:
                num_byte = 1
            elif (byte >> 4) == 0b1110:
                num_byte = 2
            elif (byte >> 3) == 0b11110:
                num_byte = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_byte -= 1

    return num_byte == 0
