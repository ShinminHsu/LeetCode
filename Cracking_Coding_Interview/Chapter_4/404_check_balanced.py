import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_balanced(root: TreeNode) -> bool:

    def helper(node):
        if not node:
            return 0

        left_height = helper(node.left)
        if left_height == -1:
            return -1

        right_height = helper(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return helper(root) != -1


def check_balanced_2(root: TreeNode) -> bool:
    if not root:
        return True

    def get_height(node):
        if not node:
            return -1
        return max(get_height(node.left), get_height(node.right)) + 1

    heightDiff = abs(get_height(root.left) - get_height(root.right))
    if heightDiff > 1:
        return False
    else:
        return check_balanced_2(root.left) and check_balanced_2(root.right)


"""
Corner case
[]
[1]
[1, 2]

[3,9,20,null,null,15,7]

1. helper(3, 0)
left_height = helper(node.left, 1) = helper(9, 1) = 
right_height = helper(node.right, 1) = helper(20, 1) = 

2. helper(9, 1)
left_height = helper(node.left, 1) = helper(9, 1) = 
right_height = helper(node.right, 1) = helper(20, 1) = 

3.
node: 20, height: 0
height = max(helper(15, 1), helper(7, 1))

"""