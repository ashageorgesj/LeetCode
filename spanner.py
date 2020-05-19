class StockSpanner:

    def __init__(self):
        self.myList = []
        self.mySpan = []
    def next(self, price: int) -> int:
        if len(self.myList) == 0:
            self.myList.append(price)
            self.mySpan.append(1)
            current = 1
        else:
            self.myList.append(price)
            prevIndex = len(self.myList) - 2
            index = prevIndex
            current = 1
            while True:
                #print(index)
                if index >= 0 and self.myList[index] <= price:
                    current +=self.mySpan[index]
                    index -= self.mySpan[index]
                else:
                    #current = 1
                    break
            self.mySpan.append(current)
        return self.mySpan[-1]
