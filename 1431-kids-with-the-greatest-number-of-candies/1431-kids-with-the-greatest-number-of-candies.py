class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum = max(candies)
        
        return [True if n + extraCandies >= maxnum else False for n in candies]