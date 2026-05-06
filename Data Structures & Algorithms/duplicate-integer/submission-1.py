class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = len(nums)
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False