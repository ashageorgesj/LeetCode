class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alienDict = {}
        valid = True
        for i,val in enumerate(order):
            alienDict[val] = i
        for i in range(0,len(words)):
            if not valid:
                break
            if (i + 1) < len(words):
                first = words[i]
                second = words[i+1]
                if len(first)<len(second):
                    first += " "*(len(second)-len(first))
                elif len(second)< len(first):
                    second += " "*(len(first)-len(second))
                #print(first,second)
                for word1,word2 in zip(first,second):
                    if word1 != " " and word2 == " ":
                        valid = False
                        break
                    elif word1 == " " and word2 != " ":
                        break
                    #print(word1,word2)
                    if alienDict[word1] > alienDict[word2]:
                        valid = False
                        break
                    elif alienDict[word1] < alienDict[word2]:
                        break
                
        return valid
