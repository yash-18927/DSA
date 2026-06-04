class Solution:
    def commonElements(self, a: list[int], b: list[int], c: list[int]) -> list[int]:
        return sorted(list(set(a) & set(b) & set(c)))
