from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        hash_map = defaultdict(lambda: 0)
        output = []

        def preorder(node):
            if not node:
                return '#'

            path = f'{node.val}-{preorder(node.left)}-{preorder(node.right)}'

            if hash_map[path] == 1:
                output.append(node)

            hash_map[path] += 1
            return path

        preorder(root)

        return output