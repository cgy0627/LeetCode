class Solution(object):
    def findKthPositive(self, arr, k):
        ans = k
        for num in arr:
            if num <= ans:
                ans += 1
            else:
                return ans
        return ans
        
#         num = 1
#         arr_set = set(arr)
#         total = len(arr)
        
#         while True:
#             arr_set -= {num}
#             if total == len(arr_set):   # doesn't exist
#                 k -= 1
#             if k == 0:
#                 return num
#             num += 1