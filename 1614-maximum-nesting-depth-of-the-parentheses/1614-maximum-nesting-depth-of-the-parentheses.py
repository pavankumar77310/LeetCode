class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        c = 0
        m = 0

        for ch in s:
            if ch in '(':
                stack.append(ch)
                c+=1
                m = max(m,c)
                
            elif ch in ')':
                stack.pop()
                c-=1
        return m