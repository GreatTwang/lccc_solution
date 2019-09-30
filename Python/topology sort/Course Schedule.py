class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        table={}
        for x in prerequisites:
            if x[1] not in table:
                table[x[1]]=[x[0]]
            else:
                table[x[1]].append(x[0])
            indegree[x[0]]+=1
        q=[]
        for i,d in enumerate(indegree):
            if d==0:
                q.append(i)
        k=0
        while q:
            node=q.pop(0)
            k+=1
            if node in table:
                for each in table[node]:
                    indegree[each]-=1
                    if indegree[each]==0:
                        q.append(each)
        return k==numCourses