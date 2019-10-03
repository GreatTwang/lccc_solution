class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            if root.left:
                p = root.left
                while p.right:
                    p = p.right
                p.right = root.right
                root.right = root.left
            root.left = None


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