class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for num in set(nums):
            n = nums.count(num)
            ans += (n * (n-1))//2
        
        return ans