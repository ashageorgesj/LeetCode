class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        base = {}
        indices = []
        for val in p:
            if val not in base:
                base[val]= 0
            base[val] += 1
        length = len(p)
        word = {}
        for i in range(0,len(s)):
            current = s[i:i+length]
            #print(current)
            if i == 0:
                for value in current:
                    if value not in word:
                        word[value]= 0
                    word[value] += 1
                if word == base:
                    indices.append(i)
            else:
                word[s[i-1]] -= 1
                if word[s[i-1]] == 0:
                    del word[s[i-1]]
                if (i+length - 1) < len(s):
                    if s[i+length - 1] not in word:
                        word[s[i+length - 1]] = 0
                    word[s[i+length - 1]] += 1
                if word == base:
                    indices.append(i)
            #print(word)
        return indices
