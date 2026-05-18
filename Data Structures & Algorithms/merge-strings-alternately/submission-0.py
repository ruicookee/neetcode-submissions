class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        string = ""
        for i in range(min_len):
            string += (word1[i] + word2[i])
        if len(word1) > len(word2):
            string += word1[min_len::]
        elif len(word1) < len(word2):
            string += word2[min_len::]
        return string
        