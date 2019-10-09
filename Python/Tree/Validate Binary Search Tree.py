#   O(N)    O(N)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        pre=float('-inf')
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                temp=stack.pop()
                if pre>=temp.val:
                    return False
                pre=temp.val
                root=temp.right
        return True