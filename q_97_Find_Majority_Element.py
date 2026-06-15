class Solution:
    def majorityElement(self, A: list[int], N: int) -> int:
        candidate = -1
        count = 0
        
        for num in A:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
                
        freq = 0
        for num in A:
            if num == candidate:
                freq += 1
                
        if freq > N // 2:
            return candidate
        return -1
