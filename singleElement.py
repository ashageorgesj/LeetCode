class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        val = -1
        if len(nums) == 1:
            return nums[0]
        for i in range(0,len(nums)-1,2):
            if nums[i]==nums[i+1]:
                continue
            val = nums[i]
            break
        if val == -1 and (len(nums) % 2 == 1):
            val = nums[-1]
        
        return val
