class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base = {}
        found = False
        for val in s1:
            if val not in base:
                base[val] = 0
            base[val] += 1
        length = len(s1)
        word = {}
        for i in range(0,len(s2)-length+1):
            current = s2[i:i+length]
            #if len(current) < length:
            #    break
            if i == 0:
                for value in current:
                    if value not in word:
                        word[value] = 0
                    word[value] += 1
                if word == base:
                    found = True
                    break
            else:
                prev = s2[i-1]
                word[prev] -= 1
                if word[prev] == 0:
                    del word[prev]
                new = current[-1]
                if new not in word:
                    word[new] = 0
                word[new] += 1
                if word == base:
                    found = True
                    break
        return found
