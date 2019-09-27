#Union find
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        def find(word):
            if word in parents:
                tmp = find(parents[word])
                parents[word] = tmp
                return tmp
            return word
        def union(parents, wd1, wd2):
            p1 = find(wd1)
            p2 = find(wd2)
            if p1 != p2:
                parents[p1] = p2
                return True
            return False
        
        if len(words1) != len(words2):
            return False
        parents = {}
        for pair in pairs:
            union(parents, pair[0], pair[1])
        for i in range(len(words1)):
            if words1[i] != words2[i] and find(words1[i]) != find(words2[i]):
                return False
        return Trues

#DFS
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        # Establish the graph
        G = collections.defaultdict(set) # use set to avoid duplicate
        for pair in pairs:
            G[pair[0]].add(pair[1])
            G[pair[1]].add(pair[0])
        # Use dfs to contruct a dictionary {word: word_root}
        similar_word = {}
        def dfs(word, word_root):
            # this function constructs a dictionary such that all similar words correspond to the same word_root
            if word in similar_word:
                return
            
            similar_word[word] = word_root
            for nb in G[word]:
                dfs(nb, word_root)
            return
                
        # construct similar_word
        for word1, word2 in zip(words1, words2):
            dfs(word1, word1)
            dfs(word2, word2)
        # examine whether words1 and words2 are similar
        for word1, word2 in zip(words1, words2):
            if similar_word[word1] != similar_word[word2]:
                return False
        return True

'''
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, 
determine if two sentences are similar.
'''