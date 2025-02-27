from typing import List

"""
encode: use a separator to separate the size of the string and the string itself
decode: loop until separator found, get the size, then get the string
"""


class Solution:
    def __init__(self):
        self.separator = "#"

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            size = len(s)
            result += str(size) + self.separator + s
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            idx = ""
            while i < len(s) and s[i] != self.separator:
                idx += s[i]
                i += 1

            size = int(idx)
            i += 1
            result.append(s[i : i + size])
            i = i + size
        return result
