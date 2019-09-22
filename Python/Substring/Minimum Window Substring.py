## O(S+T)   O(S+T)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        table = {}
        for c in t:
            table[c] = table[c]+1 if c in table else 1
        counter = len(table)
        start, end = 0, 0
        min_length = float('inf')
        while end < len(s):
            if s[end] in table:
                table[s[end]] -= 1
                if table[s[end]] == 0:
                    counter -= 1
            while counter == 0:
                if end-start+1 < min_length:
                    min_length = end-start+1
                    ans = s[start:end+1] 
                if s[start] in table:
                    table[s[start]] += 1
                    if table[s[start]] > 0:
                        counter += 1
                start += 1
            end += 1
        return ans