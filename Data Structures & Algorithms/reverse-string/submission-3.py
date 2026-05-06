class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lst = []
        for char in s:
            lst.append(char)
        
        i = 0
        while lst:
            s[i] = lst.pop()
            i += 1