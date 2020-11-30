# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionRecursive:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.findElement(root, output)
        return output

    def findElement(self, node, output):
        if node:
            self.findElement(node.left, output)
            output.append(node.val)
            self.findElement(node.right, output)

class SolutionIterative:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        output, stack = [], []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                output.append(node.val)
                node = node.right
