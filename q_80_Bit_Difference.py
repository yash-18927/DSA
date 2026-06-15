class Solution:
    def countBitsFlip(self, a: int, b: int) -> int:
        diff = a ^ b
        count = 0
        while diff > 0:
            count += diff & 1
            diff >>= 1
        return count
