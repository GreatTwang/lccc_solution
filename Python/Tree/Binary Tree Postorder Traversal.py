
# recursive   O(n)   O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root,res)
        return res
    def helper(self, root,res):
        if root==None:
            return

        if root.left:
            self.helper(root.left,res)
        if root.right:
            self.helper(root.right,res)
        res.append(root.val)

# iterative  O(n)  O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack =[root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]