class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        
        check_max = 0
        final_max = 0
        
        for i in nums:
            check_max = max(0, check_max+i)
            final_max = max(check_max, final_max)
            
        return final_max
        