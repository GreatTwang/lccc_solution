class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            node_deque = [(1,root)]
        
        while node_deque:
            depth, root = node_deque.pop(0)
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))