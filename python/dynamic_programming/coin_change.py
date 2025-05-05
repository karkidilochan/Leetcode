"""
TD approach:
recursion will return the number of coins used at each step, return 0 when target met,
add 1 to each return at the seceding step
if the main function returns float("inf"), return -1
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(total, precomputed={}):
            if total == amount:
                return 1

            # if coin not in precomputed:
            min_count = float("inf")
            for num in coins:
                cum = total + num
                if cum <= amount:
                    if cum not in precomputed:
                        result = dfs(cum)
                        precomputed[cum] = result
                    min_count = min(min_count, 1 + precomputed[cum])

            return min_count

        min_count = dfs(0)

        return -1 if min_count == float("inf") else min_count - 1


"""
BU approach:
create a table for all amounts from 0 to target
for each amount, loop through all coins, for each coin, find the no of coins needed minus the amount and add one coin
"""


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
