# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive  O(n)   O(n)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self, root,res):
        if root==None:
            return
        res.append(root.val)
        if root.left:
            self.helper(root.left,res)
        if root.right:
            self.helper(root.right,res)

# iterative  O(n)   O(n)
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res =[]
        if not root:
            return res
        stack =[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res