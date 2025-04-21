# Top-down approach: if current step exceeds the length of the cost array, return 0, we are looking for the cost only, not the path
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def dfs(i, total_cost={}):
            nonlocal cost
            if i >= len(cost):
                return 0
            if i not in total_cost:
                total_cost[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return total_cost[i]

        return min(dfs(0), dfs(1))


# Bottom-up approach:
# 1. Create a dp array of size n+1.
# 2. The first two elements of the dp array are 0, as we can start from either step 0 or step 1.
# 3. find total cost for current step by taking result of previous step, and add it with the cost of the previous step.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        result = [0] * (n + 1)
        for i in range(2, n + 1):
            result[i] = min(result[i - 1] + cost[i - 1], result[i - 2] + cost[i - 2])
        return result[n]
