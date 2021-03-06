class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """
    def search(self, A, target):
        if A is None or len(A) == 0:
            return -1
        start = 0
        end = len(A) - 1
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if A[mid] == target:
                return mid
            elif A[end] < A[mid]:
                if A[end] < target and target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        if A[end] == target:
            return end                    
        if A[start] == target:
            return start
        
        return -1

