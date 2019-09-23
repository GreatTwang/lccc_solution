//Stack
class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }        
        Stack<Character> stack = new Stack();
        for (char c : s.toCharArray()) {
            if (c == '(')
                stack.push(')');
            else if (c == '{')
                stack.push('}');
            else if (c == '[')
                stack.push(']');
            else if (stack.isEmpty() || stack.pop() != c)
                return false;
        }
        return stack.isEmpty();
    }
}




//not good
public class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() == 0) {
            return true;
        }
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if ("([{".contains(String.valueOf(c))) {//String.valueOf(c), not c !!! or use c == '(' || c == '[' || c == '{'
                stack.push(c);
                continue;
            } else {
                if (stack.empty()) {
                    return false;
                }
                char temp = stack.pop();
                if ((c == ')' && temp != '(') || (c == ']' && temp != '[') || (c == '}' && temp != '{')) {
                    return false;
                }
            }
        }
        return stack.empty();
    }
}













