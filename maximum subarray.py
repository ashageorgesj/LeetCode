# Using Kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxVal = 0
        if all([num < 0 for num in nums]):
            return max(nums)
        for i in range(0,len(nums)):
            total += nums[i]
            if total <= 0:
                total = 0
            if total > maxVal:
                maxVal = total
        return maxVal