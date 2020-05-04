# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def findHeight(root):
            if root is None:
                return 0
            
            left = findHeight(root.left)
            right = findHeight(root.right)
            self.diameter = max(self.diameter, left+right)
            return max(left, right)+1
        
        self.diameter = 0
        findHeight(root)
        return self.diameter