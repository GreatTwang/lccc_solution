## O(NK)    O(NK)  K is maxlen of all words
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=dict()
        for each in strs:
            count=[0]*26
            for c in each:
                count[ord(c)-ord('a')]+=1
            if tuple(count) in ans:
                ans[tuple(count)].append(each)
            else:
                ans[tuple(count)]=[each]
        return ans.values()