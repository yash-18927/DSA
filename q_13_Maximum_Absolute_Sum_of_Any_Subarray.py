class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix_sum = 0
        max_prefix = 0
        min_prefix = 0
        
        for num in nums:
            prefix_sum += num
            max_prefix = max(max_prefix, prefix_sum)
            min_prefix = min(min_prefix, prefix_sum)
            
        return max_prefix - min_prefix
