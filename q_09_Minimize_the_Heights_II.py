class Solution:
    def getMinDiff(self, arr: list[int], k: int) -> int:
        n = len(arr)
        if n == 1:
            return 0
        arr.sort()
        ans = arr[-1] - arr[0]
        
        tempmin = arr[0]
        tempmax = arr[-1]
        
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            tempmin = min(arr[0] + k, arr[i] - k)
            tempmax = max(arr[i-1] + k, arr[-1] - k)
            ans = min(ans, tempmax - tempmin)
            
        return ans
