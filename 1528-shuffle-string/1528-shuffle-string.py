class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        
        letters = dict(zip(indices, s))
        
        res = ""
        for i in range(len(s)):
            res += letters[i]
        
        return res