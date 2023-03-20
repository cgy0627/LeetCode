class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = sum([int(d) for n in nums for d in str(n)])
        
        
        return element_sum - digit_sum