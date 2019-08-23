class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(reversed(s.split()))
        
        k = 0
        List_word = [] 
        
        while k < len(s):
            word = ""
            while k < len(s) and s[k] == " ":
                k +=1
            while k < len(s) and s[k] != " ":
                word += s[k]
                k += 1
            if word != "":
                List_word.append(word)
                
        res = ""
        for k in range(len(List_word)-1,0,-1):
            res += List_word[k]
            res += " "
        if List_word != []:
            res += List_word[0]
        return res