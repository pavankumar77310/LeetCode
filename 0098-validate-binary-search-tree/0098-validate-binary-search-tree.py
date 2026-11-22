# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(root,left,right):
            if root is None:
                return True

            if root.val <= left or root.val >= right:
                return False

            return (check(root.left,left,root.val) and check(root.right,root.val,right))

        return check(root,float('-inf'),float('inf'))



