# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, minval, maxval):
            if not root:
                return True
            
            if minval < root.val < maxval:
                left = helper(root.left, minval, root.val)
                right = helper(root.right, root.val, maxval)
            else:
                return False
            
            return left and right
        
        return helper(root, float('-inf'), float('inf'))