class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(char) for char in str(n)]
        
        product = reduce(lambda a,b: int(a)*int(b), nums)
        total = reduce(lambda a,b: int(a)+int(b), nums)
        
        return product - total