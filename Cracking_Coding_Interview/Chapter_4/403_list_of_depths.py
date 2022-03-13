from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return

        ans, level = [], [root]
        while level:
            ans.append(node.val for node in level)
            tmp = []
            for node in level:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)

            level = tmp

        return ans