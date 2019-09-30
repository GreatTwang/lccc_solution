#   O(N)    O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # corner case
        if not root:
            return None
        q=[]        #queue
        pre=None
        q.append(root)
        # level order traversal
        while q:
            n=len(q)
            for i in range(n):
                node=q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i==0:
                    pre=node
                else:
                    pre.next=node
                    pre=node
        return root