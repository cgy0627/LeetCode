class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        res = [0] * len(boxes)
        
        for i, ball in enumerate(boxes):
            if ball == "1":
                for j in range(len(res)):
                    res[j] += abs(j-i)
        
        return res