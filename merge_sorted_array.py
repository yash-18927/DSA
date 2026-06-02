class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 as one sorted array in-place.
        
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        # Set pointers for nums1, nums2, and the end of nums1.
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        # Merge starting from the back.
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
