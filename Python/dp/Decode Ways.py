class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if s=="0":
            return 0
        nums=[0]*(n+1)
        nums[n]=1
        if s[n-1]!="0":
            nums[n-1]=1
        for i in range(n-2,-1,-1):
            if s[i]=="0":
                nums[i]=0
            else:
                nums[i]=nums[i+1]+nums[i+2] if s[i:i+2]<="26" else nums[i+1]
        return nums[0]

class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if s=="0":
            return 0
        last=1
        prev=0
        if s[n-1]!="0":
            prev=1
        for i in range(n-2,-1,-1):
            if s[i]=="0":
                curr=0
            else:
                curr=prev+last if s[i:i+2]<="26" else prev
            last=prev
            prev=curr
                     
        return prev