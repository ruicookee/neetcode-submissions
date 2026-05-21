class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### Three pointer approach
        p1 = m-1
        p2 = n-1
        last = m+n-1
        
        while p1 >= 0 and p2 >= 0: #neither nums1 nor nums2 have been emptied
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            elif nums2[p2] > nums1[p1]:
                nums1[last] = nums2[p2]
                p2 -= 1
            else: #both nums1[p1] and nums2[p2] are the same
                nums1[last] = nums1[p1]
                p1 -= 1
                last -= 1
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        
        while p1 >= 0 or p2 >= 0: #if either nums1 or nums2 emptied, but the other hasnt
            if p1 >= 0: #if nums1 hasnt been emptied
                nums1[last] = nums1[p1]
                p1 -= 1
            elif p2 >= 0: #if nums2 hasnt been emptied
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        
        return nums1