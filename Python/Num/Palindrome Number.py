class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        newx=0
        temp=x
        while temp:
            newx=newx*10+temp%10
            temp=temp//10
        return newx==x