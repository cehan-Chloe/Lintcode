class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        dp = [[0 for i in range(1 + len(A))] for j in range(1 + len(B))]
        
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] != B[j]:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                else:
                    dp[i+1][j+1] = dp[i][j] + 1
        return dp[len(A)][len(B)]
