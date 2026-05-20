class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### fit nums2 into nums1
        pointer = m
        for num in nums2:
            nums1[pointer] = num
            pointer += 1

        
        ### bubble sort nums1
        for i in range(len(nums1)-1):
            for n in range(len(nums1)-1-i):
                if nums1[n] > nums1[n+1]:
                    nums1[n], nums1[n+1] = nums1[n+1], nums1[n]
        return nums1
        