class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reversePositive(self, posi):
        reverseInt = 0
        while posi:
            reverseInt = reverseInt*10 + posi % 10
            posi /= 10
        return reverseInt
        
    def reverseInteger(self, n):
        # Write your code here
        if abs(n) > 214748364:
            return 0
        if n > 0:
            reverseInt = self.reversePositive(n)
        else:
            reverseInt = self.reversePositive(abs(n)) * -1
        return reverseInt
