#https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/581/week-3-january-15th-january-21st/3605/
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        values = [0,1]
        maxVal = max(values)
        index = 2
        while (index <= n):
            if index % 2 == 0:
                half = index // 2
                values.append(values[half])
            else:
                half = (index - 1) // 2
                values.append(values[half] + values[half + 1])
            if values[-1] > maxVal:
                maxVal = values[-1]
            index += 1
        return maxVal