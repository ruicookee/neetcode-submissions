class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        dic = {}
        for i in range(l):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else: #if nums[i] is alread in dic, check if abs(i - j) <= k
                if abs(i-dic[nums[i]]) <= k:
                    return True
                else:
                    dic[nums[i]] = i
        return False