class Solution:
    def countElements(self, arr: List[int]) -> int:
        #arr.sort()
        unique = list(set(arr))
        unique.sort()
        mydict = {}
        for val in arr:
            if val not in mydict:
                mydict[val] = 0
            mydict[val] += 1
        count = 0
        for i,val in enumerate(unique):
            if i+1 < len(unique) and unique[i] + 1 == unique[i + 1]:
                count += mydict[unique[i]]
        return count