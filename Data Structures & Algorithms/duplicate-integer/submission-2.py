class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        lst = []
        for num in nums:
            if num not in lst:
                lst.append(num)
            else:
                return True
        return False