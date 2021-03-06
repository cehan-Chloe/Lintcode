"""
Definition of ArrayReader:
class ArrayReader:
    def get(self, index):
        # this would return the number on the given index
        # return -1 if index is less than zero.
"""
class Solution:
    # @param {ArrayReader} reader: An instance of ArrayReader 
    # @param {int} target an integer
    # @return {int} an integer
    def searchBigSortedArray(self, reader, target):
        index = 1
        while reader.get(index) < target:
            index = index * 2
        start = 0
        end = index
        while start + 1 < end:
            mid = start + (end - start) / 2
            if reader.get(mid) == target:
                end =  mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if  reader.get(end) == target:
            return end
        return -1
