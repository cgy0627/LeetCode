class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums_asc = sorted(nums)
        nums_desc = nums_asc[::-1]
        
        ans = 0
        check = nums_desc.pop()
        for num in nums_asc:
            while check <= num:
                if not nums_desc:
                    ans -= 1
                    break
                check = nums_desc.pop()
                
            ans += 1
            if not nums_desc:
                break
            check = nums_desc.pop()
        
        return ans