from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level, output = [root], []

        while level:
            output.append([node.val for node in level if node])
            level = [kid for leaf in level for kid in (leaf.left, leaf.right) if kid]

        return output
