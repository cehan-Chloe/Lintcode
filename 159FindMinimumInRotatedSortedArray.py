class Solution:
    # @param num: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, num):
        # set the last element as target, and find the second ascending period
        start = 0
        end = len(num) - 1
        target = num[-1]
        while (start + 1 < end):
            mid = start + (end - start) / 2
            if num[mid] < target:
                end = mid
            else:
                start = mid
        return min(num[start], num[end])
