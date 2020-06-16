#https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3362/
class Solution:
    def validIPAddress(self, IP: str) -> str:
        values = IP.split('.')
        #print(values)
        isvp4 = False
        isvp6 = False
        if len(values) == 4:
            isvp4 = self.checkv4(values)
        if not isvp4:
            values = IP.split(':')
            if len(values) == 8:
                isvp6 = self.checkv6(values)
            
        if isvp4:
            return "IPv4"
        elif isvp6:
            return "IPv6"
        else:
            return "Neither"
            
            
    def checkv4(self,values:List[str]) -> bool:
        valid = True
        for value in values:
            if value.isdigit():
                intVal = int(value)
                # Check the range of values
                if intVal < 0 or intVal > 255:
                    valid = False
                    break
                conv = str(intVal)
                # Valid ip only if the integer converted into the string gives the original string.
                # Takes care of leading zeroes.
                if value != conv:
                    valid = False
                    break
            else:
                valid = False
                break
        return valid
    def checkv6(self,values:List[str]) -> bool:
        valid = True
        #print(values)
        for value in values:
            #print(value)
            # Checking if there are more than 4 values
            if len(value) > 4:
                valid = False
                break
            # There should be atleast one number
            if len(value) == 0:
                valid = False
                break
            # Use regular expression to check if the string follows the hexadecimal pattern
            # upper or lowercase a-f and 0-9 and the count of the numbers should have a minimum of 1
            # to a maximum of 4.
            search = (re.search(r'([A-Fa-f0-9]{1,4})',value))
            if search and len(search.group(0)) == len(value):
                intVal = int(value,16)
                if intVal < 0 and intVal > 65535:
                    valid = False
                    break
            else:
                valid = False
                break
        return valid
                
    