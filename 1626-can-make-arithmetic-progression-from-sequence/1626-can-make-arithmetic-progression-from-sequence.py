class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        diff = sorted_arr[1] - sorted_arr[0]
        for idx, num in enumerate(sorted_arr[1:], 1):
            prev_num = sorted_arr[idx - 1]
            if num - prev_num != diff:
                return False
        
        return True