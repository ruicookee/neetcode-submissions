class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for i in range(2):
            for num in nums:
                lst.append(num)
        return lst