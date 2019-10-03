cclass Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        seen=set(wordDict)
        d = [None for i in range(len(s)+1)]
        d[0] = [""]

        def dfs(i):
            if d[i] is None:
                ret=[]
                for j in range(0,i):
                    if s[j:i] in seen:
                        for head in dfs(j):
                            ret.append(head + " " + s[j:i])
                d[i]=ret
            return d[i]
        
        return [a[1:] for a in dfs(len(s))]
        