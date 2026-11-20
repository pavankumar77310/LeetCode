# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        s = []
        def dfs(root,temp,total):
            if root is None:
                return False

            temp.append(root.val)
            total+=root.val

            if root.left is None and root.right is None:
                if total == targetSum:
                    s.append(temp[:])
            else:
                dfs(root.left,temp,total)
                dfs(root.right,temp,total)

            temp.pop()

        dfs(root,[],0)
        return s
        