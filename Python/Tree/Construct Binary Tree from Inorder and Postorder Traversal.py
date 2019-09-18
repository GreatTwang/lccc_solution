class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if(not inorder):
            return None
        j = len(inorder)-1
        root = TreeNode(postorder[-1])
        stack = [root]
        cur = root
        for i in range(len(inorder)-2,-1,-1):
            if(cur.val != inorder[j]):
                stack.append(TreeNode(postorder[i]))
                cur.right = stack[-1]
                cur = cur.right
            else:
                
                while(stack and stack[-1].val == inorder[j]):
                    j -= 1
                    cur = stack.pop()
                    
                stack.append(TreeNode(postorder[i]))
                cur.left = stack[-1]
                cur = cur.left
        return root