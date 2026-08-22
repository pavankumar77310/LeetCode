class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    c+=1
        return c