class Solution:
    def countSetBits(self, n: int) -> int:
        total_bits = 0
        for i in range(1, n + 1):
            total_bits += bin(i).count('1')
        return total_bits
