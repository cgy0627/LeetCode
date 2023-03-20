class Solution:
    def distMoney(self, money: int, children: int) -> int:
        ans = 0
        if money < children:
            return -1
        if money < 8:
            return 0
        
        for i in range(children):
            if money < children or money < 8:
                break
            children -= 1
            money -= 8
            ans += 1
        
        if children == 1 & (money == 4 or money == 0):
            return ans - 1
        if children == 0 and money > 0:
            return ans - 1
        if money >= children:
            return ans

        children -= money
        if children <= 8:
            return ans - 1
        else:
            ans -= children // 8
            ans -= 1 if children % 8 > 0 else 0
            return ans
