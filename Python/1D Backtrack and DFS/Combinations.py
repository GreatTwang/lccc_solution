class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidate=[i for i in range(1,n+1)]
        res=[]
        self.dfs(candidate,0,res,[],k)
        return res
    def dfs(self,candidate,i, res,temp,k):
        if k==0:
            res.append(temp[:])
            return
        for j in range(i,len(candidate)):
            temp.append(candidate[j])
            self.dfs(candidate,j+1,res,temp,k-1)
            temp.pop()