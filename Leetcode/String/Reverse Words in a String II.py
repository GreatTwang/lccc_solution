class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reversepart(s,0,len(s)-1)
        j=0
        for i in range(len(s)):
            if s[i]==' ':
                self.reversepart(s,j,i-1)
                j=i+1
        self.reversepart(s,j,len(s)-1)
    def reversepart(self,s,start,end):
        while(start<end):
            s[start],s[end]=s[end],s[start]
            start+=1
            end-=1
 