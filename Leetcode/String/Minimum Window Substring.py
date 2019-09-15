class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = collections.defaultdict(int)
        for c in t:
            seen[c] += 1
        count = len(t)
        tail = 0
        minL = 32768
        I,J = 0,0
        for i, c in enumerate(s, 1):
            seen[c] -= 1
            if seen[c] >= 0:
                count -= 1
            if count == 0:
                while seen[s[tail]] < 0:
                    seen[s[tail]] += 1
                    tail += 1
                if i - tail  < minL:
                    minL = i - tail 
                    I,J = i, tail
        return s[J:I] if I > 0 else ""