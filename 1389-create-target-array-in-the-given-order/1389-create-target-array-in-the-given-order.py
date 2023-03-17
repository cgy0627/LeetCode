class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        
        return target
    
#         target = [0 for i in range(len(nums))]
#         for i in range(len(index)):
#             idx = index[i]
#             target = target[:idx] + [nums[i]] + target[idx:len(nums)-1]
        
#         return target
