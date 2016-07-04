class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        if len(A) < 3:
            return -1
        if len(A) == 3:
            return 1
        start = 0
        end = len(A) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            if A[mid] > A[mid - 1] and A[mid] < A[mid + 1]:
                start = mid
            if A[mid] < A[mid - 1] and A[mid] > A[mid + 1]:
                end = mid
            if A[mid] < A[mid - 1] and A[mid] < A[mid + 1]:
                end = mid
        if A[start] > A[start - 1] and A[start] > A[start + 1]:
            return start
        if A[end] > A[end - 1] and A[end] > A[end + 1]:
            return end        
            
