class Solution:
    def commonElements(self, mat: list[list[int]], r: int, c: int) -> list[int]:
        if r == 0:
            return []
            
        freq = {}
        for val in set(mat[0]):
            freq[val] = 1
            
        for i in range(1, r):
            for val in set(mat[i]):
                if val in freq and freq[val] == i:
                    freq[val] += 1
                    
        result = []
        for val, count in freq.items():
            if count == r:
                result.append(val)
        return result
