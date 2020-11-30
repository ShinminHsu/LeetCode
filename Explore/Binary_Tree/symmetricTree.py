# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True




    def checkEqual(self, node1, node2):
        """
        Check if two nodes are equal when they are leaves (no children)
        :param node1:
        :param node2:
        :return: boolean
        """
        if not node1 and not node2:
            if node1.val == node2.val:
                return True
            else:
                return False

        return self.checkEqual(node1.left, node2.right) and self.checkEqual(node1.right, node2.left)
