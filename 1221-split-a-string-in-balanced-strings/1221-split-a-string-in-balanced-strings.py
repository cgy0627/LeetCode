class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = {'R': 0, 'L': 0}
        ans = 0
        
        for char in s:
            count[char] += 1
            
            if count['R'] == count['L']:
                count['R'], count['L'] = 0, 0
                ans += 1
        
        return ans