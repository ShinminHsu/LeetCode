from collections import deque 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

NULL = '#'
NODE = '@'

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        result = []
        queue = deque([root])

        def levelOrder(node):
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(NULL)

        while any(queue):
            node = queue.popleft()
            levelOrder(node)
            
        result = NODE.join(result)
        
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(NODE)
        root = TreeNode(data[0])
        queue = deque([root])
        i = 1

        def checkChild(i):
            if i >= len(data) or data[i] == NULL:
                i += 1
                return i, None
            
            node = TreeNode(data[i])
            queue.append(node)
            i += 1

            return i, node

        while i < len(data) and queue:
            curr = queue.popleft()
            
            i, curr.left = checkChild(i)
            i, curr.right = checkChild(i)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))