class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums:
            return 0
        n = len(nums)
        # first time initializing f with 0
        f = [1] * n
        # enumerate generate an indexed series:  (0,coll[0]), (1,coll[1]) ...
        # can use enumerate to optimizite previous code
        for curr, val in enumerate(nums):
            for prev in range(curr):
                if nums[prev] <= val:
                    f[curr] = max(f[curr], f[prev] + 1)
        return max(f)
