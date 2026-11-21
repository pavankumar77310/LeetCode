class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def solve(i,temp):
            if i == len(nums):
                ans.append(temp[:])
                return
            
            temp.append(nums[i])
            solve(i+1,temp)

            temp.pop()
            solve(i+1,temp)
        solve(0,[])

        return ans