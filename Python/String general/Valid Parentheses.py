#   O(N)    O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        table={'(':')','[':']','{':'}'}
        stack=[]
        for c in s:
            if c in table:
                stack.append(table[c])
            if c in table.values():
                if stack and stack[-1]==c:
                    stack.pop()
                else:
                    return False
        return len(stack)==0


class Solution:
    def isValid(self, s: str) -> bool:
        table={'(':')',"[":"]","{":"}"}
        stack=[]
        for c in s:
            if c in table.keys():
                stack.append(table[c])
            if c in table.values():
                if c in stack:
                    stack.pop()
                else:
                    return False
        return len(stack)==0