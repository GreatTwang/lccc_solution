## O(NK)    O(NK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in ans:
                ans[tuple(count)]=[s]
            else:
                ans[tuple(count)].append(s)
        return ans.values()