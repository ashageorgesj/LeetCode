class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        guess = num//2
        #perfect = False
        while guess*guess > num:
            div = num//guess
            guess = (guess + div)//2
            #print(guess)
        if guess*guess == num:
            return True
        return False
