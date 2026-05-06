class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces = s.replace(" ","").lower()
        lst = [char for char in no_spaces if char.isalnum()]

        return lst == lst[::-1]