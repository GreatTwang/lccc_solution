class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=[]
        self.generate(s,0,0,res,n)
        return res
    def generate(self,s,l,r,res,n):
        if len(s)==2*n:
            res.append(''.join(s))
            return
        if l<n:
            s.append("(")
            self.generate(s,l+1,r,res,n)
            s.pop()
        if l>r:
            s.append(")")
            self.generate(s,l,r+1,res,n)
            s.pop()
    
# sol2: pass parameter as string
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        s=""
        self.generate(s,0,0,res,n)
        return res
    def generate(self,s,l,r,res,n):
        if len(s)==2*n:
            res.append(s)
            return
        if l<n:
            self.generate(s+"(",l+1,r,res,n)
        if l>r:
            self.generate(s+")",l,r+1,res,n)