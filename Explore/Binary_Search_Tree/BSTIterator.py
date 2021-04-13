from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):

        self.node = root
        self.visited = defaultdict(lambda: [False, False])  # node: [left, right]
        self.parent = {}  # parent: node

    def next(self) -> int:
        
        def left_dfs():
            while self.node.left is not None:
                self.parent[self.node.left] = self.node
                self.visited[self.node][0] = True
                self.node = self.node.left
            
            self.visited[self.node][0] = True
            return self.node.val
        
        # check if the left child has been visited
        if not self.visited[self.node][0]:
            return left_dfs()
            
        
        # the left child has been visited but the right child has not yet
        elif self.visited[self.node][0]:
            
            # set the right child to be visited (even though it doesn't exist)
            self.visited[self.node][1] = True  
            
            # if the right child is None, jump to the node's parent
            if self.node.right is None:
                self.node = self.parent[self.node]
                return self.node.val
            
            else:
                self.parent[self.node.right] = self.node
                self.node = self.node.right
            
                return self.next()


    def hasNext(self) -> bool:
        
        if self.node.left is None and self.node.right is None:
            node = self.node
            while self.parent[node] is not None:
                node = self.parent[node]
                if not self.visited[node][0] or not self.visited[node][1]:
                    return True
            return False
            
        return True


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
param_1 = obj.next()
param_2 = obj.hasNext()