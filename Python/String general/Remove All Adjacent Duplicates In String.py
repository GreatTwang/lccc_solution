#   O(N)    O(N)
# if c==stack top one then pop, else push into stack
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        for c in S:
            if  stack and c==stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack))
            
        