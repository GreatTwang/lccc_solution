class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            newqueue = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            res.append(node.val)
            queue = newqueue
        
        return res