class Solution(object):
    def findKthPositive(self, arr, k):
        ans = k
        for num in arr:
            if num <= ans:
                ans += 1
            else:
                return ans
        return ans