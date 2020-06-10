#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) -  1
        if len(nums) >= 1 and  target < nums[0]:
            return 0
        elif len(nums) >= 1 and target > nums[-1]:
            return len(nums)
        
        while (end - start) > 1:
            
            mid = (start + end)//2
            if nums[mid] == target:
                
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        if (end - start) <= 1:
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[start] < target < nums[end]:
                return start + 1
            elif target < nums[start]:
                return start
            elif target > nums[end]:
                return end + 1