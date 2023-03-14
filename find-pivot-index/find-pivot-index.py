class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        back = sum(nums)
        front = 0
        
        for i in range(len(nums)):
            back -= nums[i]
            if front == back:
                return i
            front += nums[i]
        
        return -1