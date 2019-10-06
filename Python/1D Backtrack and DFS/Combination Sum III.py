class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=[i for i in range(1,10)]
        res=[]
        seen=set()
        self.dfs(0,candidates,n,res,[],k,seen)
        return res
    def dfs(self,i,candidates,target,res,temp,k,seen):
        if target==0 and k==0:
            if tuple(temp[:]) not in seen:
                res.append(temp[:])
                seen.add(tuple(temp[:]))
        if k<0 or target<0:
            return
        for j in range(i,len(candidates)):
            temp.append(candidates[j])
            self.dfs(j+1,candidates,target-candidates[j],res,temp,k-1,seen)
            temp.pop()