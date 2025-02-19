from math import floor
from typing import List


def binary_search(haystack: List[int], needle: int):
    start = 0
    end = len(haystack)

    while start < end:
        midpoint = floor((start + end) / 2)
        value = haystack[midpoint]

        if value == needle:
            return True
        elif value > needle:
            end = midpoint
        else:
            start = midpoint + 1

    return False


print(binary_search([1, 2, 3, 4, 5], 6))
