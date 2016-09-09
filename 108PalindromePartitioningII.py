# class Solution:
#     # @param s, a string
#     # @return an integer
#     def minCut(self, s):
#         n = len(s)
#         if n == 0:
#             return n
#         f = []*(n+1)
#         f[0] = 0
        
#         for i in range(1,n+1):
#             tmp = []
#             for j in range(0,i):
#                 if s[i-j+1:i] == reversed(s[i-j+1:i]):
#                     tmp.append(f[j])
#             f[i] = min(tmp) + 1
#         return f[n]-1
  
# this is the second method        
# class Solution:
#     def minCut(self, s):
#         if not s:
#             return 0

#         cut = [i - 1 for i in xrange(1 + len(s))]

#         for i in xrange(1 + len(s)):
#             for j in xrange(i):
#                 if s[j:i] == s[j:i][::-1]:
#                     cut[i] = min(cut[i], 1 + cut[j])
#         return cut[len(s)]

# this question is not solved, this is the standard answer from jz
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        n = len(s)
        f = []
        p = [[False for x in range(n)] for x in range(n)]
        #the worst case is cutting by each char
        for i in range(n+1):
            f.append(n - 1 - i) # the last one, f[n]=-1
        for i in reversed(range(n)):
            for j in range(i, n):
                if (s[i] == s[j] and (j - i < 2 or p[i + 1][j - 1])):
                    p[i][j] = True
                    f[i] = min(f[i], f[j + 1] + 1)
        return f[0]
