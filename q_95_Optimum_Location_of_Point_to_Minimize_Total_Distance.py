import math

class Solution:
    def findOptimumDistance(self, line: list[int], points: list[list[int]], n: int) -> float:
        a, b, c = line[0], line[1], line[2]
        
        def get_dist(x):
            y = (-c - a * x) / b
            total_dist = 0
            for p in points:
                total_dist += math.sqrt((p[0] - x)**2 + (p[1] - y)**2)
            return total_dist
            
        low = -1000.0
        high = 1000.0
        
        for _ in range(100):
            mid1 = low + (high - low) / 3
            mid2 = high - (high - low) / 3
            
            dist1 = get_dist(mid1)
            dist2 = get_dist(mid2)
            
            if dist1 < dist2:
                high = mid2
            else:
                low = mid1
                
        return get_dist(low)
