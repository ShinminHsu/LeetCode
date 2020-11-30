from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root or root.val > sum:
            return False

        sum -= root.val
        self.queue = deque()
        self.checkLeftRight(root, sum)

        while self.queue:
            curSum, node = self.queue.pop()

            if node.val < curSum:
                self.checkLeftRight(node, curSum - node.val)

            elif (not node.left) and (not node.right) and (node.val == curSum):
                return True

        return False

    def checkLeftRight(self, node, curSum):
        if node.left <= curSum:
            self.queue.append((curSum, node.left))
        if node.right <= curSum:
            self.queue.append((curSum, node.right))





        