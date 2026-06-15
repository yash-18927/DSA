class Solution:
    def median(self, matrix: list[list[int]], r: int, c: int) -> int:
        flat_list = []
        for i in range(r):
            for j in range(c):
                flat_list.append(matrix[i][j])
        flat_list.sort()
        mid = len(flat_list) // 2
        return flat_list[mid]
