# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution1:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        if root.left:
            root.left.next = root.right
        if root.next and root.next.left:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        level_first = root
        while level_first:
            curr = level_first
            while curr:
                if curr.left:
                    curr.left.next = curr.right
                if curr.next and curr.right:
                    curr.right.next = curr.next.left

                curr = curr.next

            # set the first element to the first element in the next level
            level_first = level_first.left
            
        return root