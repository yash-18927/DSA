class Solution:
    def findTwoElement(self, arr: list[int], n: int) -> list[int]:
        counts = [0] * (n + 1)
        for val in arr:
            counts[val] += 1
            
        repeating = -1
        missing = -1
        for i in range(1, n + 1):
            if counts[i] == 2:
                repeating = i
            elif counts[i] == 0:
                missing = i
                
        return [repeating, missing]
