class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        result = 0
        i = 0
        while(i < len(s)):
            if s[i] in ["I", "X", "C"] and i != len(s)-1:
                if s[i:i+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                    result = result + roman_dict[s[i+1]] - roman_dict[s[i]]
                    #print(i, s[i:i+1], result, "ifif")
                    i += 2
                else:
                    result += roman_dict[s[i]]
                    #print(i, s[i], result, "ifelse")
                    i += 1
            else:
                result += roman_dict[s[i]]
                #print(i, s[i], result, "else")
                i += 1
            
        return result

#mySol = Solution()
#print(mySol.romanToInt("MCMXCIV"))