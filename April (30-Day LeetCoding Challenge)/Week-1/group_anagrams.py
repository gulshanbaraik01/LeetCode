class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_strs = {}
        
        for i in strs:
            sorted_s = ''.join(sorted(i))
            if sorted_s not in sort_strs:
                sort_strs[sorted_s] = [i]
            else:
                sort_strs[sorted_s].append(i)
                
        return sort_strs.values()