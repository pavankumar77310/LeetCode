class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(nums)-1
        while(l<r):
            t=nums[l]+nums[r]
            if (t==target):
                return [l+1,r+1]
            elif(t<target):
                l+=1
            else:
                r-=1
        return []