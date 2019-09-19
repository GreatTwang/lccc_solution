class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q = [root]
        res=[]
        level=0
        if not root:
            return []
        while q:
            length =len(q)
            for i in range(length):
                temp=q.pop(0)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if i==length-1:
                    res.append(temp.val)
        return res