#!/usr/bin/python3
"""
THe Prime game module
"""


def sieve_of_eratosthenes(max_num: int):
    """
    Generates all prime numbers up to a given maximum number
     using the Sieve of Eratosthenes algorithm.

    Args:
        max_num (int): The maximum number up to which primes are generated.

    Returns:
        Tuple[List[int], List[bool]]: A tuple containing:
            - A list of prime numbers up to max_num.
            - A boolean list where the index represents
                whether that number is prime.
    """
    # Initialize a list to mark prime numbers
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Implementing the Sieve of Eratosthenes algorithm
    for start in range(2, int(max_num ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_num + 1, start):
                is_prime[multiple] = False

    # Create a list of primes
    primes = [num for num, prime in enumerate(is_prime) if prime]

    return primes, is_prime


def isWinner(x, nums):
    """
    Determines the winner of the game played between Maria and Ben.

    Maria and Ben take turns picking a prime number from
    a set of consecutive integers.
    The player who cannot make a move loses.
    This function simulates x rounds of the game
    and determines which player wins the most rounds.

    Args:
        x (int): The number of rounds played.
        nums (List[int]): A list containing
        the maximum integer n for each round.

    Returns:
        Optional[str]: The name of the player who
                       wins the most rounds ("Maria" or "Ben").
                       Returns None if the result is a tie.
    """
    if not nums or x < 1:
        return None

    # Determine the maximum number in nums to
    # know the limit for primes calculation
    max_num = max(nums)

    # Generate primes up to the maximum number using Sieve of Eratosthenes
    primes, is_prime = sieve_of_eratosthenes(max_num)

    # Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Simulate each round of the game
    for n in nums:
        prime_count = 0

        # Count primes that are <= n
        for p in primes:
            if p > n:
                break
            prime_count += 1

        # Determine the winner for this round
        if prime_count % 2 == 0:
            ben_wins += 1  # Ben wins if the count is even
        else:
            maria_wins += 1  # Maria wins if the count is odd

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # Tie
