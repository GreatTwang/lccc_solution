class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res=[]
        self.dfs(0,candidates,target,res,[])
        return res
    def dfs(self,i,candidates,target,res,temp):
        if target==0:
            res.append(temp[:])
        if target<0:
            return
        for k in range(i,len(candidates)):
            temp.append(candidates[k])
            self.dfs(k,candidates,target-candidates[k],res,temp)
            temp.pop()