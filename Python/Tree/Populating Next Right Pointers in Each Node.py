class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q=[root]
        pre=None
        while q:
            n=len(q)
            for i in range(n):
                temp=q.pop(0)
                print(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)  
                if i==0:
                    pre=temp
                else:
                    pre.next=temp
                    pre=pre.next
        return root