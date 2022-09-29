class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix)-1, 0
        current = matrix[x][y]
        
        while True:
            if current == target:
                return True
            elif current > target:
                x, y = x-1, y
            elif current < target:
                x, y = x, y+1
            
            if (x < 0) | (y > len(matrix[0])-1):
                return False
            
            current = matrix[x][y]