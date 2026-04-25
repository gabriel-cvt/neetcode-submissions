# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    prev: Optional[TreeNode]
    def inOrder(self, node: Optional[TreeNode]):
        if node:
            left = self.inOrder(node.left)
            if not left:
                return False

            if self.prev:
                if self.prev.val >= node.val:
                    return False
            self.prev = node
            right = self.inOrder(node.right)
            if not right:
                return False
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inOrder(root)