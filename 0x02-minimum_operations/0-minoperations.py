#!/usr/bin/python3
"""The minimum_operations module."""
from typing import List


def is_prime(number: int) -> bool:
    """Checks if a number is prime."""
    abs_num = abs(number)

    if abs_num < 2:
        return False

    if abs_num % 2 == 0:
        return abs_num == 2

    i = 3

    while i ** 2 <= abs_num:
        if abs_num % i == 0:
            return False

        i += 2

    return True


def prime_factors(n: int) -> List[int]:
    """The function returns the prime factors of n."""
    factors = []
    if n < 2:
        factors.append(n)
        return factors

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n: int) -> int:
    """The minimum_operations function calculates
    the minimum_operations"""
    if n <= 1:
        return 0

    primes = prime_factors(n)

    min_operations = sum(primes)

    return min_operations
