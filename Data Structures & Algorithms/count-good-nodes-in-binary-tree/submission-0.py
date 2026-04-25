# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count = 0
    
    def helper(self, node: TreeNode, maxval: int):
        if not node:
            return
        if node.val >= maxval:
            maxval = node.val
            self.count += 1
        self.helper(node.left, maxval)
        self.helper(node.right, maxval)

    def goodNodes(self, root: TreeNode) -> int:
        self.helper(root, root.val)
        return self.count