class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        prev1 = prev2 = 0
        for i in nums:
            curr = max(prev1,prev2+i)
            prev2 = prev1
            prev1 = curr
        return prev1