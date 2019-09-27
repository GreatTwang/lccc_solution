class Solution:
    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        wordDict = set(wordDict)  # O(1) lookup
        word_lengths = set([len(word) for word in wordDict])  # only check actual word lengths
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:i+j] + (tail and ' ' + tail)
                           for j in word_lengths
                           if s[i:i+j] in wordDict
                           for tail in sentences(i+j)]
            return memo[i]
        return sentences(0)
        