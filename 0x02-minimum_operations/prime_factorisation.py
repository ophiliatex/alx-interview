#!/usr/bin/env python3
"""The prime factorisation module."""
from typing import List

from is_prime import is_prime


def prime_factors(n: int) -> List[int]:
    """The function returns the prime factors of n."""
    factors = []
    if n < 2:
        return factors.append(n)

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
