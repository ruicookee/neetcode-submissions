class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real_lst = [n for n in range(0,len(nums)+1)]
        for num in real_lst:
            if num not in nums:
                return num