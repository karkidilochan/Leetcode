"""
build a decision tree out of the possible actions at each element, each action can be a recursion to i+1 element with append and after pop
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []

        def run(i, total):
            if total == target:
                combinations.append(path[:])
                return
            if i >= len(candidates) or total > target:
                return

            path.append(candidates[i])
            run(i, total + candidates[i])
            path.pop()
            run(i + 1, total)

        run(0, 0)
        return combinations
