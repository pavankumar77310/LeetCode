class Solution(object):
    def threeFibonacciSum(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a,b = 0,1
        while True:
            c = a+b
            if a + b + c == n:
                return True
            elif a + b + c > n:
                return False
            a,b = b,c
        