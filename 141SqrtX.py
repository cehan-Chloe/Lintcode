class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if x < 0:
            return None
        return int(math.floor(x ** 0.5))
