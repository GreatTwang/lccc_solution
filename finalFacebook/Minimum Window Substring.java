public class Solution {
    public String minWindow(String s, String t) {
        if (s == null || t == null || s.length() < t.length()) {
            return "";
        }
        String res = "";
        int[] thash = new int[256];//thash is a dict of target chars and their occurrences
        int[] shash = new int[256];//shash records num of all chars appeared in dict that are in curr window
        for (int i = 0; i < t.length(); i++) {
            thash[t.charAt(i)]++;//build the dict
        }
        int count = 0;//num of |effective| chars in curr window,while it equals t.length(), we will try to shink the window
        int min = s.length() + 1;
        for (int left = 0, right = 0; right < s.length();) {
            char r = s.charAt(right++);
            if (thash[r] != 0) {//if it's in the dict
                shash[r]++;//num of |valid| chars in curr window increases
                if (shash[r] <= thash[r]) {//if the num of valid char is <= what target needed
                    count++;
                }
                while (count == t.length()) {
                    if (right - left < min) {//first try to update the min length and res
                        min = right - left;
                        res = s.substring(left, right);
                    }
                    char l = s.charAt(left++);
                    if (thash[l] != 0) {//if it's in the dict
                        shash[l]--;//num of |valid| chars in curr window decreses
                        if (shash[l] < thash[l]) {//if the num of valid char is < what target needed
                            count--;
                        }
                    }
                }
            }
        }
        return res;
    }
}

//if we are given a set of dict(which means each char in dict appear once)
public class Solution {
    public String minWindow(String s, HashSet<Character> thash) {
        if (s == null || t == null || s.length() < t.size()) {
            return "";
        }
        String res = "";
        int[] shash = new int[256];//shash records num of all chars appeared in dict that are in curr window
        int count = 0;//num of |effective| chars in curr window,while it equals t.length(), we will try to shink the window
        int min = s.length() + 1;
        for (int left = 0, right = 0; right < s.length();) {
            char r = s.charAt(right++);
            if (thash.contains(r)) {//if it's in the dict
                shash[r]++;//num of |valid| chars in curr window increases
                if (shash[r] == 1) {//if the num of valid char is <= what target needed
                    count++;
                }
                while (count == thash.size()) {
                    if (right - left < min) {//first try to update the min length and res
                        min = right - left;
                        res = s.substring(left, right);
                    }
                    char l = s.charAt(left++);
                    if (thash.contains(l)) {//if it's in the dict
                        shash[l]--;//num of |valid| chars in curr window decreses
                        if (shash[l] == 0) {//if the num of valid char is < what target needed
                            count--;
                        }
                    }
                }
            }
        }
        return res;
    }
}











