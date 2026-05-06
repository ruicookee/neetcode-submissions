class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = [sorted(string) for string in strs]

        final = []
        checked = []
        for i in range(len(sorted_strs)):
            set = []
            if i not in checked:
                for n in range(i, len(sorted_strs)):
                    if sorted_strs[i] == sorted_strs[n]:
                        set.append(n)
                        checked.append(n)
            
            if set:
                final.append([strs[index] for index in set])
        return final


