class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : return 0
        if len(nums) <= 2 : return max(nums)
        
        prev = 0
        curr = 0
        
        for i in nums:
            prev, curr = curr, max(curr, prev + i)
        
        return curr