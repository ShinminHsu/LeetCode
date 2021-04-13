from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i
        
        preorder_reversed = list(reversed(preorder))

        return self.helper(preorder_reversed, 0, len(preorder)-1, hash_map)

    def helper(self, preorder_reversed, in_start, in_end, hash_map):

        if in_start > in_end or not preorder_reversed:
            return None

        root = TreeNode(preorder_reversed.pop())
        root_index_inorder = hash_map[root.val]
        
        root.left = self.helper(preorder_reversed, in_start, root_index_inorder - 1, hash_map)
        root.right = self.helper(preorder_reversed, root_index_inorder + 1, in_end, hash_map)

        return root