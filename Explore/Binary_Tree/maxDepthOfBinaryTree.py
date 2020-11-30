# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.answer = 0
        return self.preorder(root, 0)

    def preorder(self, node, depth):
        if not node:
            return

        if not node.left and not node.right:
            self.answer = max(self.answer, depth)

        self.preorder(node.left, depth + 1)
        self.preorder(node.right, depth + 1)

        return self.answer

    def postorder(self, node):
        if not node:
            return 0

        left_depth = self.postorder(node.left)
        right_depth = self.postorder(node.right)

        return max(left_depth, right_depth) + 1
