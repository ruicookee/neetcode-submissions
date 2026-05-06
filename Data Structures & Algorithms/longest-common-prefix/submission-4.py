class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        l = len(strs[0])
        for i in range(0, l):
            current_letter = strs[0][i]
            for word in strs:
                if len(word) <= i or (word[i] != current_letter):
                    return prefix
            prefix += current_letter
        
        return prefix
                