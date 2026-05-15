class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #oh my god i did not read the question yikes
        nums.sort()
        length = len(nums)
        actual_sum = sum(nums)
        supposed_sum = 0
        for n in range(0, length+1):
            supposed_sum += n

        return supposed_sum - actual_sum