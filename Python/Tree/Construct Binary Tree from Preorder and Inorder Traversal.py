class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d = {}
        for i, num in enumerate(inorder):
            d[num] = i
            
        stack = []
        root = parent = None
        
        for node in preorder:
            newnode = TreeNode(node)
            
            if root is None:
                root = newnode
            elif d[newnode.val] < d[parent.val]:
                parent.left = newnode
                stack.append(parent)
            elif d[newnode.val] > d[parent.val]:
                while stack and d[newnode.val] > d[stack[-1].val]:
                    parent = stack.pop()
                parent.right = newnode
            parent = newnode

        return root