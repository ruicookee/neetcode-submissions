class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        for i in range(l-1):
            for n in range(i+1,l):
                if (nums[i] == nums[n]) and (abs(i-n)<=k):
                    return True
        return False     