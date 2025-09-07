class Solution:
    def check_if_arithmetic(self, arr: list) -> bool:
        diff = arr[1] - arr[0]
        for idx, num in enumerate(arr[1:], 1):
            prev_num = arr[idx-1]
            if num - prev_num != diff:
                return False

        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = list()
        for idx in range(len(l)):
            arr = sorted(nums[l[idx]:r[idx]+1])
            print(arr)
            ans.append(self.check_if_arithmetic(arr))
        
        return ans