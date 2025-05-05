"""
first sort to avoid duplicate combinations, build decision tree, at each recursion check if consecutive duplicates present to avoid redundant runs
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        result = []

        def run(i, total, path):
            if total == target:
                result.append(path[:])
                return

            if i >= n or total > target:
                return

            num = candidates[i]

            path.append(num)
            run(i + 1, total + num, path)
            path.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1

            run(i + 1, total, path)

        run(0, 0, [])
        return result
