class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        for i in range(0, l-1):
            for n in range(i+1, l):
                if nums[i] == nums[n]:
                    return True
        return False 