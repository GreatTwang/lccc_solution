public class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<>();
        String[] paths = path.split("/+");//split with all consecutive "/", for cases like "/home//foo" --> "/home/foo"
        for (String s : paths) {
            if (s.equals("..")) {// /../ means going back to the last directory,so we pop out one directory if !stack.empty() 
                if (!stack.empty()) {
                    stack.pop();
                }
            } else if (!s.equals(".") && !s.equals("")) {// /./ means curr directory, so we don't need to do anything
                stack.push(s);//if it's not "." or "", we just add the directory to stack
            }
        }
        String res = "";
        while (!stack.empty()) {//we build string from sub directory to root directory,so res it's added at the end of string
            res = "/" + stack.pop() + res;
        }
        if (res.length() == 0) {//if it's empty (eg. /../, or /home/../), we need to return "/"
            return "/";
        }
        return res;
    }
}




