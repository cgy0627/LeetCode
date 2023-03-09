class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for num in nums:
            if num:
                count += 1
            else:
                max_ones = max(max_ones, count)
                count = 0
        
        return max(max_ones, count)
        