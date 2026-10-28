class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        temp = n
        while temp%3 == 0:
            temp = temp//3

        if temp == 1:
            return True
        else:
            return False