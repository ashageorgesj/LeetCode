#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

class Solution:

    def __init__(self, w: List[int]):
        self.weights = w
        self.indices = list(range(0,len(w)))

    def pickIndex(self) -> int:
        return random.choices(self.indices,weights=self.weights,k=1)[0]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()