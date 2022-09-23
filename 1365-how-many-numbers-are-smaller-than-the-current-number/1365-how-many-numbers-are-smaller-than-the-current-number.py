class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = dict()
        for i, n in enumerate(sorted(nums)):
            if n not in res:
                res[n] = i
        
        return [res[n] for n in nums]