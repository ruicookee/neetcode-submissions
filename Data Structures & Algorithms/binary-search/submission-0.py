class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p1, p2 = 0, len(nums)-1

        while p1 <= p2:
            mid = p1 + ((p2-p1)//2)

            if nums[mid] > target:
                p2 = mid - 1
            elif nums[mid] < target:
                p1 = mid + 1
            else: #if nums[mid] == target:
                return mid
        return -1


