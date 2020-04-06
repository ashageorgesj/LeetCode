class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        minVal = min(prices)
        maxVal = max(prices)
        myList = []
        start = 0
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1]:
                myList.append(prices[start:i+1])
                start = i + 1
        if start < len(prices):
            myList.append(prices[start:])
        for member in myList:
            if len(member) >= 2:
                profit += max(member) -  min(member)
        return profit
