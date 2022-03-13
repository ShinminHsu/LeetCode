class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def successor(target: TreeNode) -> TreeNode:

    if not target:
        return None

    if target.right:
        return leftMostChild(target.right)
    else:
        parent = target.parent
        # go up until we are on the left instead of right
        while parent and parent.left != target:
            target = parent
            parent = parent.parent

        return parent

def leftMostChild(node: TreeNode):
    if not node:
        return None
    while node.left:
        node = node.left

    return node
