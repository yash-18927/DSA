class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_num = 0
        for num in nums:
            unique_num ^= num
        return unique_num
