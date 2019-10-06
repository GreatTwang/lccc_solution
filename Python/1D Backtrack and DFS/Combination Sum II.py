class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res=[]
        seen=set()
        self.dfs(0,candidates,target,res,[],seen)
        return res
    def dfs(self,i,candidates,target,res,temp,seen):
        if target==0:
            if tuple(temp[:]) not in seen:
                res.append(temp[:])
                seen.add(tuple(temp[:]))
        if target<0:
            return
        for k in range(i,len(candidates)):
            temp.append(candidates[k])
            self.dfs(k+1,candidates,target-candidates[k],res,temp,seen)
            temp.pop()