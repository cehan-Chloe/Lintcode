class Solution:
    # @param n a integer
    # @return ans a integer
    
    # the first method is time limit exceeded
    
    # def factorial(self,n):
    #     product = 1
    #     while n > 0:
    #         product *= n
    #         n -= 1
    #     return product
        
    # def trailingZeros(self, n):
    #     product = self.factorial(n)
    #     zeroNum = 0
    #     while product % 10 == 0:
    #         zeroNum += 1
    #         product /= 10
    #     return zeroNum
    
    
    # second method: 0 can only be caused by 5*2/10. 10 is also a product of 5 and an even number
    def trailingZeros(self,n):
        sum = 0
        while n is not 0:
            n /= 5
            sum += n
        return sum
