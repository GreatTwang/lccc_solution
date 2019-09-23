class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = {}
        seen = set()
        for i,x in enumerate(s):
            if x not in d:
                if t[i] in seen:
                    return False
                seen.add(t[i])
                d[x] = t[i]
            elif d[x] != t[i]:
                return False
        return True