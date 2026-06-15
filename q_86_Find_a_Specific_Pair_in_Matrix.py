class Solution:
    def findMaxValue(self, mat: list[list[int]], n: int) -> int:
        max_val = -float('inf')
        max_mat = [[0] * n for _ in range(n)]
        max_mat[n-1][n-1] = mat[n-1][n-1]
        
        for j in range(n-2, -1, -1):
            max_mat[n-1][j] = max(mat[n-1][j], max_mat[n-1][j+1])
            
        for i in range(n-2, -1, -1):
            max_mat[i][n-1] = max(mat[i][n-1], max_mat[i+1][n-1])
            
        for i in range(n-2, -1, -1):
            for j in range(n-2, -1, -1):
                diff = max_mat[i+1][j+1] - mat[i][j]
                if diff > max_val:
                    max_val = diff
                max_mat[i][j] = max(mat[i][j], max(max_mat[i+1][j], max_mat[i][j+1]))
                
        return max_val
