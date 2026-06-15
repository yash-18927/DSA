class Solution:
    def search(self, arr: list[int], n: int, x: int, k: int) -> int:
        i = 0
        while i < n:
            if arr[i] == x:
                return i
            diff = abs(arr[i] - x)
            jump = max(1, diff // k)
            i += jump
        return -1
