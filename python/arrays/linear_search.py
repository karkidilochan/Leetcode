from typing import List


def linear_search_pythonic(haystack: List[int], needle: int) -> bool:
    return needle in haystack


def linear_search(haystack: List[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            return True

    # or you could do it in even more grounded way
    for i in range(len(haystack)):
        if haystack[i] == needle:
            return True
    return False


print(linear_search_pythonic([1, 2, 3, 4, 5], 4))
print(linear_search([1, 2, 3, 4, 5], 4))
