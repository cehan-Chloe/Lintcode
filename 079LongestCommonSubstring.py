class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.

    def longestCommonSubstring(self, A, B):
        n = 0
        for i in range(len(A)):
            for j in range(len(B)):
                l = 0
                # from different starter but the same string length
                while i + l < len(A) and j + l < len(B) and A[i + l] == B[j + l]:
                    l += 1
                if l > n:
                    n = l
        return n
