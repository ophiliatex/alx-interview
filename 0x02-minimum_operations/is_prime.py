#!/usr/bin/env python3
"""The is_prime function checks if a number is prime."""


def is_prime(number: int) -> bool:
    """Checks if a number is prime."""
    abs_num = abs(number)

    if abs_num < 2:
        return False

    if abs_num % 2 == 0:
        return abs_num == 2

    i = 3

    while i ** 2 <= abs_num:
        if i % abs_num == 0:
            return False

        i += 2

    return True
