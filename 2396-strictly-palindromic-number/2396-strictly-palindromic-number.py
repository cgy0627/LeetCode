class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
                    
        def num_base(num, base):
            ans = ''
            
            while num:
                num, m = divmod(num, base)
                ans = str(m) + ans

            return ans

        def is_num_palindromic(num):
            num = str(num)
            length = len(num)

            if length % 2 == 0:   # even
                if num[:length//2] == num[length//2:][::-1]:
                    return True
            else:
                if num[:length//2] == num[length//2 + 1:][::-1]:
                    return True

            return False
        
        for i in range(2, n-1):
            if not is_num_palindromic(num_base(n, i)):
                return False
        
        return True
