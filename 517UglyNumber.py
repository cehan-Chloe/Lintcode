class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
 
    def isUgly(self, num):
        # Write your code here
        # negative numver are attributed to False
        if num < 1:
            return False
        if num >= 1 and num <= 5:
            return True
        while num >= 2 and num % 2 == 0:
            num /= 2;  
        while num >= 3 and num % 3 == 0:
            num /= 3;  
        while num >= 5 and num % 5 == 0:
            num /= 5;  
        return num == 1
