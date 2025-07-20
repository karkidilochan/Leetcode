# runtime: 4^n, space: O(n)
# take each phone number, create a path from its letter, backtrack for each succeeding digit


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []

        def recurse(idx, path):
            if idx >= len(digits):
                result.append("".join(path))
                return
            number = digits[idx]

            for letter in phone[number]:
                path.append(letter)
                recurse(idx + 1, path)
                path.pop()

        if len(digits) > 0:
            recurse(0, [])

        return result
