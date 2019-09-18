class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        carry = 0
        curr = 0
        s=''
        while (i>=0 or j>=0):
            x = int(a[i]) if i>=0 else 0
            y = int(b[j]) if j>=0 else 0
            curr = (x + y + carry)%2
            carry=(x + y + carry)//2
            s=str(curr)+s
            if i>=0:
                i-=1
            if j>=0:
                j-=1
        if carry:
            s='1'+s
        return s



        