# time O(n) space O(1)
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s: return False
        s=s.strip()                         # strip the heading and tailing spaces of the string
        res = signs = eE = dot = False
        for c in s:
            if '0'<=c<='9':                 # current is number
                res=True                    # seen number
                signs=True                  # not more signs
            elif c=='.' and not dot:        # current is dot, not seen dot before
                dot=True                    # no more dots
                signs=True                  # no more signs
            elif (c=='e' or c=='E') and (not eE) and res: 
                # current is e, not seen e before, seen number before
                res=False                   # have to see number after e
                signs=False                 # can see more signs
                dot=True                    # not more dot
                eE=True # not more e
            elif (c=='+' or c=='-') and not res and not signs:
                # current is sign, not seen number before, not seen sign before
                signs=True                  # no more signs
            else:
                return False
        return res