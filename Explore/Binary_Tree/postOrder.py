# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.output = []

        def findElement(node, output):
            if node:
                findElement(node.left, output)
                findElement(node.right, output)
                output.append(node.val)

        findElement(root, self.output)

        return self.output
