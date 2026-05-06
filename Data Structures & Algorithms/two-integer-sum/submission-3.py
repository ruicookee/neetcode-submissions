class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = [] 
        for i, num in enumerate(nums):
            lst.append([num, i])
        lst.sort()

        p1 = 0
        p2 = len(lst)-1
        while lst[p1][0]+lst[p2][0] != target:
            if lst[p1][0]+lst[p2][0] < target:
                p1 += 1
            elif lst[p1][0]+lst[p2][0] > target:
                p2 -= 1
        return [min(lst[p1][1], lst[p2][1]), max(lst[p1][1], lst[p2][1])]
