"""
Dont get anxious about stacks, think of them as a data structure to look backwards
keep a count of open and close parentheses,
if open remains, add open and recurse,
backtrack and check if close can be added; close<open
if open == close == n, add to result
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def run(open, close):
            if open == close == n:
                result.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                run(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                run(open, close + 1)
                stack.pop()

        run(0, 0)
        return result
