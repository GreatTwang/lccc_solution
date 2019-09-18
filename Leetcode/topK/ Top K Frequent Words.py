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
