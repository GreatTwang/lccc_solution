class BSTIterator(object):
    
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.treeStack = []
        while root != None:
            self.treeStack.append(root)
            root = root.left
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.treeStack) != 0
        

    def next(self):
        """
        :rtype: int
        """
        node = self.treeStack.pop()
        if node.right != None:
            node2 = node.right
            while node2 != None:
                self.treeStack.append(node2)
                node2 = node2.left
        return node.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())