# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderRec(self, node: Optional[TreeNode], level: int, arr: [int]):
        if not node:
            return
        
        if len(arr) <= level:
            arr.append([])

        arr[level].append(node.val)

        self.levelOrderRec(node.left, level + 1, arr)
        self.levelOrderRec(node.right, level + 1, arr)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        self.levelOrderRec(root, 0, array)
        return array
        