class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        length = len(A)
        f = [[] for i in range(length)]
        f[0] = True
        for i in range(length):
            if f[i] == True and A[i] + i < length:
                for j in range(i,A[i] + i + 1):
                    f[j] = True
            elif f[i] == True and A[i] + i >= length:
                f[length-1] = True
        for i in range(length):
            if f[i] != True:
                f[i] = False
        return f[length-1]
        
