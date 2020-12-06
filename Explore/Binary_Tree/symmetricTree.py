from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionIterative:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root or (not root.left and not root.right):
            return True

        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            node1, node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
                
            elif (not node1 and node2) or (node1 and not node2) or (node1.val != node2.val):
                """
                if node1 is None but node2 is not, or the opposite, or the values of these two nodes are different
                """
                return False

            queue.append((node1.right, node2.left))
            queue.append((node1.left, node2.right))
        
        return True

class SolutionRecursive:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.isMirror(root.left, root.right)

        
    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2:
            return False

        if node1.val == node2.val:
            outPair = self.isMirror(node1.left, node2.right)
            inPair = self.isMirror(node1.right, node2.left)

            return outPair and inPair

        return False


        