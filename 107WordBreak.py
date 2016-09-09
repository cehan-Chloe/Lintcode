class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # initialize
        n = len(s)
        # the first method these checks are forgot
        if n == 0 and len(dict) == 0:
            return True
        elif len(dict) == 0:
            return False
                
        f = [False] * (n+1)
        f[0] = True
        # this is the first method and time limit execeed 88% pass
        # for i in range(1, n+1):
        #     for j in range(i):
        #         if s[j:i] in dict and f[j]:
        #             f[i] = True
        # return f[n]
        maxLength = max([len(w) for w in dict])
        for i in range(1, n+1):
            for j in range(1,min(i, maxLength) + 1):
                if s[i-j:i] in dict and f[i-j]:
                    f[i] = True
        return f[n]
