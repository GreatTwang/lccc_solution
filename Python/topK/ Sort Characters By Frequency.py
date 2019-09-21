#Given a string, sort it in decreasing order based on the frequency of characters.
class Solution:
    def frequencySort(self, s: str) -> str:
        sortstr=str()
        freqlist=list()
        for i in set(s):
            freqlist.append((s.count(i),i))
        freqlist=sorted(freqlist)[::-1]
        for i in freqlist:
            sortstr=sortstr+i[0]*i[1]
        return sortstr
                    
        return result

# bucket sort
class Solution:
    def frequencySort(self, s: str) -> str:
        word_dict={}
        bucket =[[] for i in range(len(s)+1)]
        for char in s:
            word_dict[char] = word_dict.get(char, 0) + 1
            
        for key, value in word_dict.items():
            if bucket[value] is None:
                bucket[value] = []
            
            bucket[value].append(key)
        
        result=""
        for i in range(len(bucket)-1,-1,-1):
            if bucket[i] is not None:
                for char in bucket[i]:
                    result += char * i
                    
        return result
        