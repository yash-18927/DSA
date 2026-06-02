class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = current_max = nums[0]
        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_so_far = max(max_so_far, current_max)
        return max_so_far
