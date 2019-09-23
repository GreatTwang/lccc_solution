## O(S+T)   O(S+T)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        table = {}
        for c in p:
            table[c] = table[c]+1 if c in table else 1
        counter = len(table)
        start, end = 0, 0
        while end < len(s):
            if s[end] in table:
                table[s[end]] -= 1
                if table[s[end]] == 0:
                    counter -= 1
            while counter == 0:
                if end-start+1==len(p):
                    ans.append(start)
                if s[start] in table:
                    table[s[start]] += 1
                    if table[s[start]] > 0:
                        counter += 1
                start += 1
            end += 1
        return ans