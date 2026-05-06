class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return [num for i in range(2) for num in nums]