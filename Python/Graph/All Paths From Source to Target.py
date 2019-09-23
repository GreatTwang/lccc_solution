#Input: [[1,2], [3], [3], []] 
#Output: [[0,1,3],[0,2,3]] 
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        path=[0]
        self.dfs(0,graph,path,res)
        return res
    
    def dfs(self,node,graph,path,res):
        if node==len(graph)-1:
            res.append(path[:])
            return
        if not graph[node]:
            return
        for each in graph[node]:
            path.append(each)
            self.dfs(each,graph,path,res)
            path.pop()