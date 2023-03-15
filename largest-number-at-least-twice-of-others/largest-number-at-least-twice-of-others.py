class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first, second, max_idx = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] > first:
                first, second = nums[i], first
                max_idx = i
            else:
                if nums[i] > second:
                    second = nums[i]
        
        if first >= second * 2:
            return max_idx
        return -1