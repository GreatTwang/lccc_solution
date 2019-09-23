//StringBuilder
public class Solution {
    public String countAndSay(int n) {
        if (n < 1) {
            return "";
        }
        StringBuilder prev = new StringBuilder("1");//"1", not 1 !!!
        for (int i = 1; i < n; i++) {
            StringBuilder curr = new StringBuilder();
            int count = 0;//record the num of curr repeating char
            char c = prev.charAt(0);//record curr repeating char
            for (int j = 0; j < prev.length(); j++) {
                if (j != 0 && prev.charAt(j) != prev.charAt(j - 1)) {//&&, not || !!!
                    curr.append(count + "").append(c);
                    c = prev.charAt(j);//update curr char
                    count = 0;//update the count
                }
                count++;//increment counter
            }
            curr.append(count + "").append(c);//remember to add the last repeating char
            prev = curr;
        }
        return prev.toString();
    }
}








