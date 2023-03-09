class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        mag = Counter(magazine)
        
        for char in ransomNote:
            if char in mag:
                mag[char] -= 1
                
                if mag[char] < 0:
                    return False
            else:
                return False
        
        return True