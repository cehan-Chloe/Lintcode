class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # find the position whose value is equal or more than target
        # only consider no duplicates conditions
        if len(A) == 0:
            return 0
        start = 0
        end = len(A) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid
        if A[start] >= target:
            return start
        if A[end] >= target:
            return end
        # must can find a position to insert
        # if target is more than all the elements of array, return len(A)
        # insert it into the tail of array
        return len(A)
