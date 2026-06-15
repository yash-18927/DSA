class Solution:
    def findPair(self, n: int, x: int, arr: list[int]) -> bool:
        seen = set()
        for num in arr:
            if (num - x) in seen or (num + x) in seen:
                return True
            seen.add(num)
        return False
