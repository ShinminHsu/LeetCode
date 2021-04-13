
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution1:
    def connect(self, root: 'Node') -> 'Node':

        level_first = root

        while level_first:
            level_first, curr, last = None, level_first, None

            while curr:
                if not level_first:
                    level_first = curr.left or curr.right

                if curr.left:
                    if last:
                        last.next = curr.left
                    last = curr.left

                if curr.right:
                    if last:
                        last.next = curr.right
                    last = curr.right

                curr = curr.next

        return root
            
            


class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
            
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = self.helper(root.next)

        elif root.right:
            root.right.next = self.helper(root.next)

        self.connect(root.left)
        self.connect(root.right)

        return root


    def helper(self, node: 'Node'):

        if not node:
            return None

        while node:
            if node.left:
                return node.left
            elif node.right:
                return node.right
            node = curr.next

        return None