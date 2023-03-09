class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        
        res = 0
        for person in accounts:
            wealth = sum(person)
            if wealth > res:
                res = wealth
        
        return res