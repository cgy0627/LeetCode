class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        points = sorted(points, key=lambda x: (x[0],x[1]))
        
        answer = []
        for query in queries:
            x, y, r = query
            count = 0
            
            for point in points:
                px, py = point
                
                if (px >= x + r) & (py >= y + r):
                    break
                
                if r >= ((px-x)**2 + (py-y)**2)**0.5:
                    count += 1
            
            answer.append(count)
        
        return answer