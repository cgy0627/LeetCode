class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
                    
        def num_base(num, base):
            ans = ''
            d, m = divmod(num, base)
            return '100'
            while d:
                ans = str(m) + ans
                
                d, m = divmod(d, base)

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
