
## O(NlogN)  O(N)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.data=[]
        self.preorder(root,0,0)
        # sort by data[2],then by reverse order data[1],then data[0]
        self.data.sort(key=lambda x:x[2])
        self.data.sort(key=lambda x:x[1], reverse=True)
        self.data.sort(key=lambda x:x[0])
        ans={}
        for d in self.data:
            if d[0] not in ans:
                ans[d[0]]=[d[2]]
            else:
                ans[d[0]].append(d[2])
        return ans.values()
    def preorder(self,node,x,y):
        if not node:
            return
        self.data.append((x,y,node.val)) 
        self.preorder(node.left,x-1,y-1)
        self.preorder(node.right,x+1,y-1)