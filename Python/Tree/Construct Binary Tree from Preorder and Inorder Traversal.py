class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if not inorder:
            return None
        ele = preorder.pop(0)
        root = TreeNode(ele)
        idx = inorder.index(ele)
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

class Solution(object):
    def buildTree(self, preorder, inorder):
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