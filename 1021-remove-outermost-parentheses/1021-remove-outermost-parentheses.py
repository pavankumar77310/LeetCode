class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        co = 0
        for c in s:
            if c == '(':
                if co > 0:
                    ans += c
                co += 1

            else:
                co -= 1
                if co > 0:
                    ans += c
        return ans