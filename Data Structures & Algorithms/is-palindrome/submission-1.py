class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_spaces = s.replace(" ","").lower()
        lst = [char for char in no_spaces if self.alphanumeric(char)]

        return lst == lst[::-1]

    def alphanumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))        