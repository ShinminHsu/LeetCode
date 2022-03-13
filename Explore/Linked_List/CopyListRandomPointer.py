# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # make the copy of each node and link them side by side
        iteration = head
        while iteration:
            next = iteration.next
            copy  = Node(iteration.val)

            iteration.next = copy
            copy.next = next

            iteration = iteration.next.next


        # assign the random nodes to the copy nodes
        iteration = head
        while iteration:
            if iteration.random:
                iteration.next.random = iteration.random.next  # copy.random = random

            iteration = iteration.next.next

        # remove the original nodes
        newHead = iteration = head.next
        while iteration:
            iteration.next = iteration.next.next
            iteration = iteration.next


        return newHead