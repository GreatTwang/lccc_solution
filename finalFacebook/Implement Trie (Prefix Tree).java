// insert / search / startsWith: O(wordLength) time; O(numOfTrieNode * 26) = O(numOfWords * wordLength * 26) space
class TrieNode {
    TrieNode[] children;
    boolean isWord;
    
    public TrieNode() {
        children = new TrieNode[26];//an 26 size array to show the next chars that are available 
        isWord = false;//show whether is a word or a prefix, or both in some cases
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            int j = word.charAt(i) - 'a';//charAt(i), not charAt(j) !!!
            if (node.children[j] == null) {
                node.children[j] = new TrieNode();
            }
            node = node.children[j];
        }
        node.isWord = true;//remember to mark its isWord true
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            int j = word.charAt(i) - 'a';
            if (node.children[j] == null) {
                return false;
            }
            node = node.children[j];
        }
        return node.isWord;//node.isWord, not isWord !!! finally we need to make sure it's a word, not a prefix
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for (int i = 0; i < prefix.length(); i++) {//prefix, not word !!!
            int j = prefix.charAt(i) - 'a';
            if (node.children[j] == null) {
                return false;
            }
            node = node.children[j];
        }
        return true;//no matter it's a word or a prefix, we should return true
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");









