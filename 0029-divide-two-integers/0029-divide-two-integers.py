class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        a, b = abs(dividend), abs(divisor)
        ans = 0

        while a >= b:
            temp, count = b, 1

            while a >= (temp << 1):
                temp <<= 1
                count <<= 1

            a -= temp
            ans += count

        if (dividend < 0) != (divisor < 0):
            ans = -ans

        return ans