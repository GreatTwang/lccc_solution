class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        n = len(s)
        f = [False for i in range(n+1)]
        f[0] = True
        for i in range(n):
            if f[i]:
                for j in wordDict:
                    l = len(j)
                    if i+l<=n and s[i:i+l] == j:
                        f[i+l] = True
        return f[n]
    