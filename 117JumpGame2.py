class Solution:
    # @param A, a list of integers
    # @return an integer
    
    # DP, the first method can only pass 70%
    # def jump(self, A):
    #     if not A:
    #         return 0
    #     n = len(A)
    #     f = [[]for i in range(n)]
    #     f[0] = 0
    #     # the function is hard to get
    #     for i in range(1,n):
    #         for j in range(i+1):
    #             if A[j] >= i - j:
    #                 f[i] = min(f[i],f[j] + 1)
    #     return f[-1]
    
    # this method from leetcode discuss
    def jump(self, A):
        # ret is the num of steps
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret
