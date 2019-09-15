class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        ppid_dict= collections.defaultdict(list)
        for i in range(len(ppid)):
            ppid_dict[ppid[i]].append(pid[i])
        if kill not in pid:
            return []
        queue = [kill]
        res=[]
        while queue:
            x = queue.pop(0)
            res.append(x)
            if x in ppid_dict:
                for each in ppid_dict[x]:
                    queue.append(each)
        return res