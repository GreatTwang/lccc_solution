class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack=[]
        pre=None
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                temp=stack.pop()
                if pre and pre.val>=temp.val:
                    return False
                pre=temp
                root=temp.right
        return True