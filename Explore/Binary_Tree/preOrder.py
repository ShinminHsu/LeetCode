# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# recursively
class SolutionRecursive:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.findElement(root, output)
        return output

    def findElement(self, node, output):
        if node:
            output.append(node.val)
            self.findElement(node.left, output)
            self.findElement(node.right, output)

# iteratively
class SolutionInterative:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        output, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                # stack: FILO -> append right first which will be popped last
                stack.append(node.right)
                stack.append(node.left)
        return output
