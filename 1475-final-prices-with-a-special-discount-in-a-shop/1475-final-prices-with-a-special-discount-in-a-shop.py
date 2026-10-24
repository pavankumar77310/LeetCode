class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        ans = []

        for i in range(len(prices)):
            dis = 0

            for j in range(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    dis = prices[j]
                    break
            
            ans.append(prices[i] - dis)
        return ans