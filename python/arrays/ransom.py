class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        magazine_map = Counter(magazine)

        for c in ransomNote:
            if c not in magazine_map or magazine_map[c] == 0:
                return False
            magazine_map[c] -= 1
        return True
