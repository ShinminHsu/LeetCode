# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        targets = [p.val, q.val]

        def helper(node):
            if not node:
                return None

            if node.val in targets:
                return node

            left = helper(node.left)
            right = helper(node.right)

            # if both left and right child match, then return node (their parents)
            if left and right:
                return node
            else:
                return left or right

        return helper(root)