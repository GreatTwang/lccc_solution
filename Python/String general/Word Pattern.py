class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        if len(words) != len(pattern):
            return False
        dic = {}
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]] != words[i]:
                    return False
            else:
                if words[i] in seen:
                    return False
                else:
                    dic[pattern[i]] = words[i]
                    seen.add(words[i])
        else:
            return True