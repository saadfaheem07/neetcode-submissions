class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 0x7FFFFFFF
        if b == 0:
            return a if a <= maxInt else ~(a ^ mask)

        sum = a ^ b
        carry = (a & b) << 1

        return self.getSum(sum & mask,carry & mask)