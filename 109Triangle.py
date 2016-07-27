class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    # the first method is divide & conquer. it works but time limit exceeded
    
    # def triangleSum(self, x, y, triangle):
    #     if x + 1 >= self.length:
    #         return triangle[x][y]
    #     left = self.triangleSum(x+1, y, triangle)
    #     right = self.triangleSum(x+1, y+1, triangle)
    #     return min(left, right) + triangle[x][y]
        
        
    # def minimumTotal(self, triangle):
    #     if triangle is None:
    #         return 0
    #     self.length = len(triangle)
    #     return self.triangleSum(0, 0, triangle)
     
    # the second method i use DP and from top to buttom
    def minimumTotal(self, triangle):
        # initialize
        length = len(triangle)
        # the method to use python to initialize an empty 2D matrix
        # cannot initialize as 0, the rules below would use 0 to generate the full f[][]
        f = [[[] for i in range(length)] for j in range(len(triangle[length - 1]))]
        f[0][0] = triangle[0][0]
        
        # rules
        for x in range(1, length):
            f[x][0] = f[x - 1][0] + triangle[x][0]
            f[x][x] = f[x - 1][x - 1] + triangle[x][x]
        for i in range(1, length):
            for j in range(i+1):
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]
                
        # reach the bottom
        return min(f[length - 1])
