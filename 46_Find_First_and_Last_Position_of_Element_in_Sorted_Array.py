class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_first(nums: list[int], target: int) -> int:
            low = 0
            high = len(nums) - 1
            first_idx = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first_idx = mid
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first_idx
            
        def find_last(nums: list[int], target: int) -> int:
            low = 0
            high = len(nums) - 1
            last_idx = -1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last_idx = mid
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last_idx
            
        return [find_first(nums, target), find_last(nums, target)]
