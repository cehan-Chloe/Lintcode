class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        carryNum = 1
        if digits[len(digits) - 1] + 1 < 10:
            digits[len(digits) - 1] += 1
            return digits
        for i in reversed(range(0,len(digits))):
            if digits[i] + carryNum >= 10:
                digits[i] = 0 
                carryNum = 1
            else:
                digits[i] += 1
                carryNum = 0
                return digits
        digits.insert(0, 1)
        return digits
            
