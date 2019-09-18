# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursion  O(n)  O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    
    def helper(self, root, res):
        if root == None:
            return
        if root.left:
            self.helper(root.left,res)
        res.append(root.val)
        if root.right:
            self.helper(root.right,res)

# iteration  O(n)  O(n)
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        stack =[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res