class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        numSet = set()
        while n != 1 and n not in numSet:
            numSet.add(n)
            sum = 0
            while n:
                num = n % 10
                sum += num * num
                n /= 10
            n = sum
        # if n is 1:
        #     return True
        # else:
        #     return False
        
        # a better method
        return n == 1
    
