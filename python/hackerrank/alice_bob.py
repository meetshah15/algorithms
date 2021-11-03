#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sillyGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def isPrime(n):
    if n == 1: return False

    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False

    return True


def searchPrime(n):
    for i in n:
        if isPrime(i):
            return i
    return False


def sillyGame(n):
    winner = False # Bob, Alice - True
    prime_exists = True
    number_list = [i for i in range(1, n + 1)]

    while prime_exists:
        new_prime = searchPrime(number_list)
        remove = []
        if not new_prime: break
        for i in range(new_prime - 1, len(number_list)):
            if i % new_prime:
                remove.append(i)

        for values in remove:
            number_list.remove(values)

        winner = not winner

    if winner:
        return "Alice"
    else:
        return "Bob"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        result = sillyGame(n)
        print(result)
