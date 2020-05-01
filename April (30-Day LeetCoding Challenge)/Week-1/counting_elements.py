class Solution:
    def countElements(self, arr: List[int]) -> int:
        set1 = set(arr)
        count = 0
        
        for i in arr:
            if (i+1) in set1:
                count += 1
                
        return count