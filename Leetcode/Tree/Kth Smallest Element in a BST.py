class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack, count = [], 0
        while len(stack) or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                else:
                    root = node.right
        return None
