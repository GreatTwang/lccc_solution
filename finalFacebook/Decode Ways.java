// O(N) time O(1) space dp solution
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {//remember to add s.charAt(0)=='0' !!!eg."0" should return 0
            return 0;
        }
        int c1 = 1;//decode ways of s[i-1]
        int c2 = 1;//decode ways of s[i-2]
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                c1 = 0;//if s.charAt(i) is 0, it can't be used as a single digit, so set c1 = 0
            }
            if (s.charAt(i - 1) == '1' || (s.charAt(i - 1) == '2' && s.charAt(i) <= '6')) {
                c1 = c1 + c2;//if s.charAt(i) and s.charAt(i-1) can work together as a digit, update c1 to c1+c2
                c2 = c1 - c2;//update c2 to previous c1
            } else {//if s.charAt(i) can only work as a single digit,no new decode ways are added,eg.12 has 2 ways,123 is same
                c2 = c1;//c1 = c1 is omitted, update c2 = c1
            }
        }
        return c1;
    }
}
// O(n) time O(N) space dp solution
public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];//num of ways of decoding s.substring(0, i)
        dp[0] = 1;
        dp[1] = s.charAt(0) != '0' ? 1 : 0;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if (first >= 1 && first <= 9) {//can form a one-digit num
                dp[i] += dp[i-1];  
            }
            if (second >= 10 && second <= 26) {//can form a two-digit num
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}

// dfs O(n) time O(n) stack space
// check every 1 or 2 chars, if can be a double, skip 1 or 2 chars and solve the rest; else,skip 1 char and solve the rest
// if string the first char is '0', directly return 0
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) {//if the initial string is empty, return 0 !!! not 1 !!!
            return 0;
        }
        return helper(s, 0);
    }
    
    private int helper(String s, int index) {
        if (s.length() == index) {//if the whole string has been decoded, return 1
            return 1;
        }
        if (s.charAt(index) == '0') {
            return 0;
        }
        if (s.length() - 1 > index && isValidDouble(s.substring(index, index + 2))) {//if it can, there will be two ways of decoding curr substring
            return helper(s, index + 1) + helper(s, index + 2);
        } else {//there is only one way to decode
            return helper(s, index + 1);
        }
    }
    
    private boolean isValidDouble(String s) {//check whether the 2 chars can form a valid two digit number
        return s.charAt(0) == '1' || (s.charAt(0) == '2' && s.charAt(1) <= '6' && s.charAt(1) >= '0');
    }
}

//return all decode ways:
public class Solution {
    public List<String> numDecodings(String s) {
        List<String> res = new ArrayList<>();
        if (s == null || s.length() == 0) {//if the initial string is empty, return 0 !!! not 1 !!!
            return res;
        }
        helper(res, s, new StringBuilder(), 0);
        return res;
    }
    
    private void helper(List<String> res, String s, StringBuilder path, int index) {
        if (s.length() == index) {//if the whole string has been decoded, return 1
            res.add(path.toString());
            return;
        }
        if (s.charAt(index) == '0') {
            return;
        }
        int length = path.length();
        //first way of decoding by 1-digit num
        int num1 = Integer.valueOf(s.substring(index, index + 1));
        path.append((char)('A' + num1 - 1));
        helper(res, s, path, index + 1);
        path.setLength(length);
        if (s.length() - 1 > index && isValidDouble(s.substring(index, index + 2))) {//if it can, there will be another way of decoding curr substring by 2-digit num
            int num2 = Integer.valueOf(s.substring(index, index + 2));
            path.append((char)('A' + num2 - 1));
            helper(res, s, path, index + 2);
            path.setLength(length);
        }
    }
    
    private boolean isValidDouble(String s) {//check whether the 2 chars can form a valid two digit number
        return s.charAt(0) == '1' || (s.charAt(0) == '2' && s.charAt(1) <= '6' && s.charAt(1) >= '0');
    }
}

//if can use '*'
public class Solution'*' {
    int M = 1000000007;
    public int numDecodings(String s) {
        long first = 1, second = s.charAt(0) == '*' ? 9 : s.charAt(0) == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            long temp = second;
            if (s.charAt(i) == '*') {
                second = 9 * second;
                if (s.charAt(i - 1) == '1')
                    second = (second + 9 * first) % M;
                else if (s.charAt(i - 1) == '2')
                    second = (second + 6 * first) % M;
                else if (s.charAt(i - 1) == '*')
                    second = (second + 15 * first) % M;
            } else {
                second = s.charAt(i) != '0' ? second : 0;
                if (s.charAt(i - 1) == '1')
                    second = (second + first) % M;
                else if (s.charAt(i - 1) == '2' && s.charAt(i) <= '6')
                    second = (second + first) % M;
                else if (s.charAt(i - 1) == '*')
                    second = (second + (s.charAt(i) <= '6' ? 2 : 1) * first) % M;
            }
            first = temp;
        }
        return (int) second;
    }

}


// if A to Z should be can decoded by 0 to 25? then we don't need to separately consider the case 0
// O(1) space dp solution
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0 || s.charAt(0) == '0') {//remember to add s.charAt(0)=='0' !!!eg."0" should return 0
            return 0;
        }
        int c1 = 1;//decode ways of s[i-1]
        int c2 = 1;//decode ways of s[i-2]
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == '1' || (s.charAt(i - 1) == '2' && s.charAt(i) <= '5')) {
                c1 = c1 + c2;//if s.charAt(i) and s.charAt(i-1) can work together as a digit, update c1 to c1+c2
                c2 = c1 - c2;//update c2 to previous c1
            } else {//if s.charAt(i) can only work as a single digit,no new decode ways are added,eg.12 has 2 ways,123 is same
                c2 = c1;//c1 = c1 is omitted, update c2 = c1
            }
        }
        return c1;
    }
}
// O(n) space dp solution
public class Solution {
    public int numDecodings(String s) {
        if(s == null || s.length() == 0) {
            return 0;
        }
        int n = s.length();
        int[] dp = new int[n+1];//num of ways of decoding s.substring(0, i)
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i <= n; i++) {
            int first = Integer.valueOf(s.substring(i-1, i));
            int second = Integer.valueOf(s.substring(i-2, i));
            if (first >= 0 && first <= 9) {//can form a one-digit num
                dp[i] += dp[i-1];  
            }
            if (second >= 10 && second <= 25) {//can form a two-digit num
                dp[i] += dp[i-2];
            }
        }
        return dp[n];
    }
}

// dfs O(n) time O(n) stack space
// check every 1 or 2 chars, if can be a double, skip 1 or 2 chars and solve the rest; else,skip 1 char and solve the rest
public class Solution {
    public int numDecodings(String s) {
        if (s == null || s.length() == 0) {//if the initial string is empty, return 0 !!! not 1 !!!
            return 0;
        }
        return helper(s, 0);
    }
    
    private int helper(String s, int index) {
        if (s.length() == index) {//if the whole string has been decoded, return 1
            return 1;
        }
        if (s.length() - 1 > index && isValidDouble(s.substring(index, index + 2))) {//if it can, there will be two ways of decoding curr substring
            return helper(s, index + 1) + helper(s, index + 2);
        } else {//there is only one way to decode
            return helper(s, index + 1);
        }
    }
    
    private boolean isValidDouble(String s) {//check whether the 2 chars can form a valid two digit number
        return s.charAt(0) == '1' || (s.charAt(0) == '2' && s.charAt(1) <= '5' && s.charAt(1) >= '0');
    }
}

//return all decode ways:
public class Solution {
    public List<String> numDecodings(String s) {
        List<String> res = new ArrayList<>();
        if (s == null || s.length() == 0) {//if the initial string is empty, return 0 !!! not 1 !!!
            return res;
        }
        helper(res, s, new StringBuilder(), 0);
        return res;
    }
    
    private void helper(List<String> res, String s, StringBuilder path, int index) {
        if (s.length() == index) {//if the whole string has been decoded, return 1
            res.add(path.toString());
            return;
        }
        int length = path.length();
        int num1 = Integer.valueOf(s.substring(index, index + 1));
        path.append((char)('A' + num1 - 1));
        helper(res, s, path, index + 1);
        path.setLength(length);
        if (s.length() - 1 > index && isValidDouble(s.substring(index, index + 2))) {//if it can, there will be another way of decoding curr substring
            int num2 = Integer.valueOf(s.substring(index, index + 2));
            path.append((char)('A' + num2 - 1));
            helper(res, s, path, index + 2);
            path.setLength(length);
        }
    }
    
    private boolean isValidDouble(String s) {//check whether the 2 chars can form a valid two digit number
        return s.charAt(0) == '1' || (s.charAt(0) == '2' && s.charAt(1) <= '6' && s.charAt(1) >= '0');
    }
}









