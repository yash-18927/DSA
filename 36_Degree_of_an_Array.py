class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first_occurrence = {}
        last_occurrence = {}
        frequency = {}
        
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            frequency[num] = frequency.get(num, 0) + 1
            
        degree = max(frequency.values())
        min_length = len(nums)
        
        for num, count in frequency.items():
            if count == degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
                
        return min_length
