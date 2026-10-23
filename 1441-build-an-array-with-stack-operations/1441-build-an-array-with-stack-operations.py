class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans = []
        x = 1

        for num in target:
            while x < num:
                ans.append("Push")
                ans.append("Pop")
                x += 1

            ans.append("Push")
            x += 1

        return ans