class Solution:
    def decodeString(self, s: str) -> str:
        res=""
        stack=[]
        num=""
        for i in range(len(s)):
            c=s[i]
            if c.isdigit():
                num+=c
                continue
            if c=="[":
                stack.append(["",int(num)])
                num=""    
                continue           
            if c=="]":
                word, times=stack.pop()
                if stack:
                    stack[-1][0]+=word*times
                else:
                    res+=word*times
                continue
            if stack:
                stack[-1][0]+=c
            else:
                res+=c
        return res