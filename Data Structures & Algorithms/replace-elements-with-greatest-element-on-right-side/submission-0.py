class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):

            largest = -1
            for n in range(i+1, len(arr)):
                
                if arr[n] > largest:
                    largest = arr[n]
            arr[i] = largest
        return arr
