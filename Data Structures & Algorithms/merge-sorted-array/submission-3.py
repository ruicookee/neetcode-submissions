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
            else: # if nums2[p2] is bigger than or equal, if its equal then it will loop back again anyway
                nums1[last] = nums2[p2]
                p2 -= 1
            last -= 1
        
        while p2 >= 0: #only nums2 will ever be not emptied because in nums1, the remaining number will already be in place
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1
        
        return nums1