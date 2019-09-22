#find longest word in dictionary that can be built using characters in array s
class Solution:    
    def check(self,s1,s2):
        table={}
        for c in s2:
            table[c]=table.get(c,0)+1
        for c in s1:
            if c in s2:
                table[c]-=1
                if table[c]<0:
                    return False
            else:
                return False
        return True

    def longest(self,s,words):
        words.sort(key=lambda x:len(x),reverse=True)
        print(words)
        for word in words:
            if self.check(word,s):
                return word
        return None