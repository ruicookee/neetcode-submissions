class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst = []
        for char in operations:
            if char == "+":
                lst.append(lst[-1] + lst[-2])
            elif char == "D":
                lst.append(lst[-1]*2)
            elif char == "C":
                lst = lst[0:len(lst)-1]
            else:
                lst.append(int(char))
        return sum(lst)



