class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        arithmetic_count = 0
        diff = 0
        for idx, num in (enumerate(nums[1:], 1)):
            if arithmetic_count == 0:
                diff = num - nums[idx-1]
                arithmetic_count += 1
                continue

            if num - nums[idx-1] != diff:
                diff = num - nums[idx-1]
                arithmetic_count = 1
                continue
            
            arithmetic_count += 1
            ans += arithmetic_count - 1
        
        return ans