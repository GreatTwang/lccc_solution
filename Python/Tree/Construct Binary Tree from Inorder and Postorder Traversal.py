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
    def buildTree(self, inorder, postorder):
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