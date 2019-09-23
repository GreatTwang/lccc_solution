public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        int m = haystack.length();
        int n = needle.length();
        for (int i = 0; i <= m - n; i++) {//we use m - n to reduce time; should be <=, not < !
            int j = 0;
            for (; j < n; j++) {
                if (haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }
            }
            if (j == n) {
                return i;//should be i, not i + j !
            }
        }
        return -1;
    }
}

//find the first index in haystack that starts with an anagram of needle
//assume only lowercase letters in strings
//O(mn) time, O(m) space
public class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        int m = haystack.length();
        int n = needle.length();
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i <= m - n; i++) {//we use m - n to reduce time; should be <=, not < !
            String key = createKey(haystack, i, n);
            if (!map.containsKey(key)) {
                map.put(key, i);
            }
        }
        String target = createKey(needle, 0, n);
        if (map.containsKey(target)) {
            return map.get(target);
        }
        return -1;
    }
    
    private String createKey(String s, int start, int length) {
        int[] count = new int[26];//see this as O(1) space
        for (int i = 0; i < length; i++) {//O(n) time
            count[s.charAt(start + i) - 'a']++;
        }
        String key = "";
        for (int j = 0; j < count.length; j++) {//see this as O(1) time
            if (count[j] != 0) {
                key += String.valueOf(count[j]) + String.valueOf((char)('a' + j));
            }
        }
        return key;
    }
}










