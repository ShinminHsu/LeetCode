
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node): #DFS iteratively
        if not node:
            return node
        hash_table = {node: Node(node.val)}
        stack = [node]
        while stack:
            n = stack.pop()
            
            for neighbor in n.neighbors:
                if neighbor not in hash_table:
                    stack.append(neighbor)  # append for later search
                    hash_table[neighbor] = Node(neighbor.val)  # generate a new object and save in hash_table
                    
                hash_table[n].neighbors.append(hash_table[neighbor])  # append the new object into the neighbors of n
                
        return hash_table[node]