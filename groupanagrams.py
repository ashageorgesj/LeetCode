class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        output = []
        for string in strs:
            alphaDict = {}
            for alpha in string:
                if alpha not in alphaDict:
                    alphaDict[alpha] = 0
                alphaDict[alpha] += 1
            keys = list(alphaDict.keys())
            keys.sort()
            dictKey = ""
            for key in keys:
                dictKey += key + str(alphaDict[key])
            if dictKey not in mydict:
                mydict[dictKey] =[]
            mydict[dictKey].append(string)
        for value in mydict.values():
            output.append(value)
        return output