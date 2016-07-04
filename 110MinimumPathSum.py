class Solution:
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j - 1]
                elif i > 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                # at first, i use else instead of elif i > 0 and j > 0. Have ignored the situation that i == 0 and j == 0 is different
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[len(grid) - 1][len(grid[0]) - 1]
