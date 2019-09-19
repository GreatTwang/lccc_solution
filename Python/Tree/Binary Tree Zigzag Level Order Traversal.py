class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q=[root]
        res=[]
        level=0
        sign=0
        while q:
            length=len(q)
            res.append([])
            if level%2:
                sign=0
            else:
                sign=length-1
            for i in range(length):
                temp=q.pop(0)
                res[level].insert(sign,temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            level+=1
        return res