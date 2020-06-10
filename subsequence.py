#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s== t:
            return True
        if len(s) == 0:
            return True
        count = 0
        output = []
        for val in t:
            if len(s) > count and val == s[count]:
                output.append(val)
                count += 1
        if len(output) > 0:
            if ''.join(output) == s:
                return True
        return False