from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        if (not root.left) and (not root.right) and (root.val == sum):
            return True

        sum -= root.val
        self.queue = deque()
        self.checkLeftRight(root, sum)

        while self.queue:
            node, curSum = self.queue.pop()
            if (not node.left) and (not node.right) and (node.val == curSum):
                return True
            
            self.checkLeftRight(node, curSum - node.val)

        return False

    def checkLeftRight(self, node, curSum):
        if node.left:
            self.queue.append((node.left, curSum))
        if node.right:
            self.queue.append((node.right





        