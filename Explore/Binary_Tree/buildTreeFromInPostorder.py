from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given two integer arrays inorder and postorder 
    where inorder is the inorder traversal of a binary tree 
    and postorder is the postorder traversal of the same tree, 
    construct and return the binary tree.
    """

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        # build a hash map for finding index faster
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i

        return self.helper(inorder, postorder, 0, len(inorder)-1, hash_map)

    def helper(self, postorder, in_start, in_end, hash_map):
        
        if in_end < in_start or not postorder:
            return None

        root = TreeNode(postorder.pop())
        inorder_root_index = hash_map[root.val]

        # we need to start from right tree, since the root of right tree will be in the last few elements in postorder
        root.right = self.helper(postorder, inorder_root_index + 1, in_end, hash_map)
        root.left = self.helper(postorder, in_start, inorder_root_index - 1,  hash_map)
        
        return root

inorder = [1,5,2,3,9,7,10]
postorder = [1,2,5,9,10,7,3]

s = Solution()
s.buildTree(inorder, postorder)