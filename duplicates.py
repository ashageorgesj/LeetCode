class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i,val in enumerate(nums):
            if val in nums[0:i]:
                return val
        