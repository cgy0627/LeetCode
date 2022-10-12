class Solution:
    def repeatedCharacter(self, s: str) -> str:
        first = {}
        
        for char in s:
            if char in first:
                return char
            else:
                first[char] = 1