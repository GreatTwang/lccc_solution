class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table={}
        for i in range(len(order)):
            table[order[i]]=i
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            l1=len(w1)
            l2=len(w2)
            for i in range(min(l1,l2)):
                if table[w1[i]]<table[w2[i]]:
                    break
                elif table[w1[i]]>table[w2[i]]:
                    return False
                elif l1>l2:
                    return False
        return True