#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        halfLength = len(s)//2
        length = len(s)
        for i in range(0,halfLength):
            first = s[i]
            s[i] = s[length - i - 1]
            s[length - i - 1] = first