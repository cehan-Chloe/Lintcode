class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        f = [[] for i in range(n + 1)]
        # now i still don't know why f[0] should be 1
        if i == 0:
            return 1
        if i == 1:
            return 1
        if i == 2:
            return 2
        f[1] = 1
        f[2] = 2
        # because they can only take one stair or two stars to f[i] and the path won't be the same because the last step is different!
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2] 
        return f[n]
        
        
