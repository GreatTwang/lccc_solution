#Given a non-empty list of words, return the k most frequent elements.
#Your answer should be sorted by frequency from highest to lowest. 
#If two words have the same frequency, then the word with the lower alphabetical order comes first.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = {}
        for word in words:
            if word in frequencies:
                frequencies[word] += 1
            else:
                frequencies[word] = 1
        keys = list(frequencies.keys())
        keys.sort(key = lambda x: (-frequencies[x], x))
        return keys[:k]
