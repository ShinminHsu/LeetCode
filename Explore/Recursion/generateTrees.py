from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        memo = {}
        
        def helper(start, end, memo):

            if start > end:
                return [None]

            if (start, end) in memo:
                return memo[(start, end)]

            result_list = []

            for i in range(start, end+1):

                left_list, right_list = helper(start, i-1, memo), helper(i+1, end, memo)

                for left in left_list:
                    for right in right_list:

                        root, root.left, root.right = TreeNode(i), left, right
                        result_list.append(root)

            memo[(start, end)] = result_list
            return result_list

        if n == 0:
            return []

        return helper(1, n, memo)
                         