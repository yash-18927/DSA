class Solution:
    def kthSmallest(self, mat: list[list[int]], n: int, k: int) -> int:
        flat_list = []
        for i in range(n):
            for j in range(n):
                flat_list.append(mat[i][j])
        flat_list.sort()
        return flat_list[k-1]
