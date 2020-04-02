class Solution:
    def isHappy(self, n: int) -> bool:
        happy = False
        myList = []
        current = str(n)
        squares = [(int(member))**2 for member in current]
        total = sum(squares)
        while total != 1 and total not in myList:
            myList.append(total)
            current = str(total)
            squares = [int(member)**2 for member in current]
            total = sum(squares)
           
        if total == 1:
            happy = True
        return happy
        
        