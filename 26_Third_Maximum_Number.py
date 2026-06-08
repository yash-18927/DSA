class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        first_max = None
        second_max = None
        third_max = None
        
        for num in nums:
            if num in (first_max, second_max, third_max):
                continue
                
            if first_max is None or num > first_max:
                third_max = second_max
                second_max = first_max
                first_max = num
            elif second_max is None or num > second_max:
                third_max = second_max
                second_max = num
            elif third_max is None or num > third_max:
                third_max = num
                
        if third_max is None:
            return first_max
            
        return third_max
