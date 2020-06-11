# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3357/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        twos = 0
        for val in nums:
            if val == 0:
                zeros += 1
            elif val == 1:
                ones += 1
            else:
                twos += 1
        #print(zeros,ones,twos)
        for i,val in enumerate(nums):
            #print(nums,zeros,ones,twos)
            if zeros > 0:
                nums[i] = 0
                zeros -= 1
            elif ones > 0:
                nums[i] = 1
                ones -= 1
            elif twos > 0:
                nums[i] = 2
                twos -= 1