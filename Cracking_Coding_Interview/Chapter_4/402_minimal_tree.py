class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minumalTree(nums) -> TreeNode:

    def helper(nums):

        if not nums:
            return None

        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = helper(nums[:mid])
        node.right = helper(nums[mid+1:])

        return node

    return helper(nums)