class Solution:
    def countBits(self, num: int) -> List[int]:
        bits = {}
        bits[0] = 1
        if num == 0:
            return [0]
        values = [0]
        #count = 0
        current = 1
        for i in range(1,num+1):
            
            if i == current:
                bits[i] = 1
                values.append(1)
                #count += 1
                current = current * 2
                
            else:
                diff = i - (current//2)
                #print(i,diff)
                if diff in bits:
                    values.append(1 + bits[diff])
                    bits[i] = 1 + bits[diff]
        return values
