class Solution:
    def getMinMax(self, arr: list[int], n: int) -> list[int]:
        if n == 0:
            return []
        if n == 1:
            return [arr[0], arr[0]]
            
        if arr[0] < arr[1]:
            min_val = arr[0]
            max_val = arr[1]
        else:
            min_val = arr[1]
            max_val = arr[0]
            
        for i in range(2, n):
            if arr[i] > max_val:
                max_val = arr[i]
            elif arr[i] < min_val:
                min_val = arr[i]
                
        return [min_val, max_val]
