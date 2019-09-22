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