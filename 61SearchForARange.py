class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if A is None or len(A) == 0:
            return[-1,-1]
        start = 0
        end = len(A) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if A[mid] == target:
                end = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            left = start
        elif A[end] == target:
            left = end
        else:
            return[-1,-1]
        
        start = left
        end = len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if A[mid] == target:
                start = mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        if A[end] == target:
            right = end 
        ''' one tip: cannot use another if, because there maybe two continuous same num. so A[start] and A[end] maybe the same and the value of A[start] may override the right value
        '''
        elif A[start] == target:
            right = start
        return [left,right]
