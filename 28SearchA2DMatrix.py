class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            line = mid / n
            column = mid % n
            if matrix[line][column] == target:
                return True
            elif matrix[line][column] < target:
                start = mid
            else:
                end = mid
        if matrix[(start / n)][(start % n)] == target:
            return True
        if matrix[(end / n)][(end % n)] == target:
            return True
        return False

