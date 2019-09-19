class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        s = [self.length(x)+x for x in strs]
        return ''.join(s)
    
    def length(self,s):
        l=len(s)
        res=[]
        while l:
            res.insert(0,str(l%10))
            l=l//10
        while len(res)<4:
            res.insert(0,'0')
        return ''.join(res)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        i=0
        n=len(s)
        res=[]
        while(i<n):
            l=int(s[i:i+4])
            i+=4
            res.append(s[i:i+l])
            i+=l
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))