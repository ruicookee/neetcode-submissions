class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        new_sorted = sorted(dict.items(), key=lambda item: item[1], reverse=True)
        
        lst = []
        while k > 0:
            lst.append(new_sorted[k-1][0])
            k-=1
        
        return lst