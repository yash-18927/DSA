class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split_with_max_sum(max_sum: int) -> bool:
            subarrays_count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > max_sum:
                    subarrays_count += 1
                    current_sum = num
                    if subarrays_count > k:
                        return False
                else:
                    current_sum += num
            return True
            
        low = max(nums)
        high = sum(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_split_with_max_sum(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
