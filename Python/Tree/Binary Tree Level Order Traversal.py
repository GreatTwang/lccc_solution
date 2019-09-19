## iterative
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = [root]
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.pop(0)
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels
# recursive
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels