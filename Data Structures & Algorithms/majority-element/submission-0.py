class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] = 1
        
        val = len(nums)/2
        for key, value in d.items():
            if value > val:
                return key
