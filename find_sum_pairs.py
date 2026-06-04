class FindSumPairs:
    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counts = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old = self.nums2[index]
        self.nums2[index] += val
        self.counts[old] -= 1
        self.counts[old + val] += 1

    def count(self, tot: int) -> int:
        return sum(self.counts[tot - x] for x in self.nums1)
