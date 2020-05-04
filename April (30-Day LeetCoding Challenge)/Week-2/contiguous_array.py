class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        check_dict = {0: 0}
        
        for i, num in enumerate(nums, 1):
            if num==0:
                count -= 1
            else:
                count += 1
                
            if count in check_dict:
                max_length = max(max_length, i - check_dict[count])
            else:
                check_dict[count] = i
        
        return max_length