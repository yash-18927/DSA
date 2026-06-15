class Solution:
    def rowWithMax1s(self, arr: list[list[int]], n: int, m: int) -> int:
        max_idx = -1
        max_count = 0
        
        for i in range(n):
            current_count = 0
            for j in range(m):
                if arr[i][j] == 1:
                    current_count += 1
            if current_count > max_count:
                max_count = current_count
                max_idx = i
                
        return max_idx
