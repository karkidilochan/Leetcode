"""
TOP-DOWN APPROACH: Memoization

1. Create a memoization array to store computed values
2. Initialize the first two values of the array
3. Iterate through the array and compute the value of each index
4. Return the last value of the array
"""


def fibonacci(n, precomputed={}):
    if n == 0 or n == 1:
        return n
    if n not in precomputed:
        precomputed[n] = fibonacci(n - 1, precomputed) + fibonacci(n - 2, precomputed)
    print(precomputed[n])
    return precomputed[n]


"""
BOTTOM-UP APPROACH: Tabulation

1. Create a tabulation array to store computed values
2. Initialize the first two values of the array
3. Iterate through the array and compute the value of each index
4. Return the last value of the array
"""


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[-1]
