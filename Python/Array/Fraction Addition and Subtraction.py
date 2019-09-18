class Solution:
    def fractionAddition(self, expression: str) -> str:
        A=0
        B=1
        if expression == '':
            return ''
        if expression[0]!='-':
            expression = "+"+expression
        i = 0
        while i < len(expression):
            symbol = expression[i]
            j = i+1
            while expression[j]!="/":
                j+=1
            m = j+1
            while m<len(expression) and expression[m] not in '+-':
                m += 1
            a = int(expression[i+1:j])
            b = int(expression[j+1:m])
            if symbol == "+":
                A = A*b + B*a
            else:
                A = A*b - B*a 
            B = B*b
            i = m
        gcd = abs(self.gcd(A,B))
        A //= gcd
        B //= gcd
        return str(A)+"/"+str(B)
    
    def gcd(self, a, b):
        if b==0:
            return a 
        else:
            return self.gcd(b,a%b)