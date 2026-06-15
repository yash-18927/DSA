class Solution:
    def sortedMatrix(self, N: int, Mat: list[list[int]]) -> list[list[int]]:
        flat_list = []
        for i in range(N):
            for j in range(N):
                flat_list.append(Mat[i][j])
        
        flat_list.sort()
        
        idx = 0
        result = []
        for i in range(N):
            row = []
            for j in range(N):
                row.append(flat_list[idx])
                idx += 1
            result.append(row)
            
        return result
