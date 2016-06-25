class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # they are different
        if A is None or len(A) == 0:
            return -1
        # set start and end
        end = len(A) - 1
        start = 0
        # while loop, use start + 1 < end to avoid dead loop
        while (start + 1 < end):
            mid = start + ( end - start ) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                # start..mid..end, target in start..mid
                end = mid
            else:
                start = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
