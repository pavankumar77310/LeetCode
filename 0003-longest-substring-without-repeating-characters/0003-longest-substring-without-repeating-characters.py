class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        temp = ""
        l = 0
        n = len(s)
        for r in range(n):
                if s[r] in temp:
                    temp = temp[temp.index(s[r])+1:]
                    l+=1

                temp += s[r]
                ans = max(ans,len(temp))

        return ans