class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[[] for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        f[0][0] = 1
        for i in range(1,m):
            if obstacleGrid[i][0] == 1:
                f[i][0] = 0
            else:
                f[i][0] = f[i-1][0]
        
        for j in range(1,n):
            if obstacleGrid[0][j] == 1:
                f[0][j] = 0
            else:
                f[0][j] = f[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    f[i][j] = 0
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[m-1][n-1]
