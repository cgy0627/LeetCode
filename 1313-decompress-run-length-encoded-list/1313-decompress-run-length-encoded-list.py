class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans += [nums[i+1] for k in range(nums[i])]
        
        return ans