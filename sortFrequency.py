class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = {}
        for val in s:
            if val not in mydict:
                mydict[val] = 0
            mydict[val] += 1
        new = sorted(mydict.items(),key=lambda item:item[1],reverse=True)
        alphabets = [member[0] for member in new for i in range(member[1])]
        return ''.join(alphabets)
        
        
