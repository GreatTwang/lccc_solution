#  O(n)    O(n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k]=reversed(a[i:i+k])
        return ''.join(a)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a=list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k]=self.reversestr(a[i:i+k])
        return ''.join(a)
    
    def reversestr(self,s):
        i=0
        j=len(s)-1
        s1=[x for x in s]
        while(i<j):
            s1[i],s1[j]=s1[j],s1[i]
            i+=1
            j-=1


