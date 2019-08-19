class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(' : ')', '[' : ']', '{' : '}'}
        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if len(stack) == 0 or dic[stack.pop()] != c:
                    return False
        return len(stack) == 0