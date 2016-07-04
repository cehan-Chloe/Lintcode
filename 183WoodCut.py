class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def pieces(self, L, length):
        p = 0
        for i in L:
            p += i / length
        return p
        
    def woodCut(self, L, k):
        # at first, this if check condition is ignored
        if sum(L) < k:
            return 0
        start = 1
        end = max(L)
        while start + 1 < end:
            mid = start + (end - start) / 2
            if self.pieces(L, mid) >= k:
                start = mid
            else:
                end = mid
        if self.pieces(L, end) >= k:
            return end
        return start
                
