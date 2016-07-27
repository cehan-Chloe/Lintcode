class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        # at first the initializing is wrong,because the first for loop should generate column and the second for loop should generate line
        f = [[[] for i in range(n)] for j in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1,m):
            f[i][0] = f[i-1][0] + grid[i][0]
        for j in range(1,n):
            f[0][j] = f[0][j-1] + grid[0][j]
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = min(f[i-1][j],f[i][j-1]) + grid[i][j]
        return f[m-1][n-1]
        
        # sample method, no extra space
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if i == 0 and j > 0:
        #             grid[i][j] += grid[i][j - 1]
        #         elif i > 0 and j == 0:
        #             grid[i][j] += grid[i - 1][j]
        #         elif i > 0 and j > 0:
        #             grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        # return grid[len(grid) - 1][len(grid[0]) - 1]
