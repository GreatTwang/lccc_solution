class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        self.helper(root, pre)
    
    def helper(self, root, pre):
        if not root:
            return pre
        pre = self.helper(root.right, pre)
        pre = self.helper(root.left, pre)
        
        root.right = pre
        root.left = None
        pre = root
        return root


'''
    1       
   / \
  2   5
 / \   \
3   4   6
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''