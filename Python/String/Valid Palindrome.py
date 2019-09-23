class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while(i<j):
            if(s[i].isalnum() and s[j].isalnum()):
                if(s[i].lower() != s[j].lower()):
                    return False
                i+=1
                j-=1
            elif(not s[i].isalnum()):
                i+=1
            elif(not s[j].isalnum()):
                j-=1
        return True