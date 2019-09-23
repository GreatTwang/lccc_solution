//recursive O(C^K) = O(length of mappings' string ^ length of digits) time; O(1) hash + O(length of digits) stack space
public class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return res;
        }
        HashMap<Character, String> map = new HashMap<>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        helper(res, map, digits, new StringBuilder(), 0);
        return res;
    }
    
    private void helper(List<String> res, HashMap<Character, String> map, String digits, StringBuilder path, int index) {
        if (index == digits.length()) {
            res.add(path.toString());//remember to add toString !!!
            return;//remember to return after adding the res !!!!
        }
        String letters = map.get(digits.charAt(index));
        int length = path.length();
        for (int i = 0; i < letters.length(); i++) {
            path.append(letters.charAt(i));
            helper(res, map, digits, path, index + 1);
            path.setLength(length);
        }
    }
}
//http://www.programcreek.com/2014/04/leetcode-letter-combinations-of-a-phone-number-java/

//iterative O(C^K)=O(CK * C^K) time I guess; O(length of mappings' string ^ length of digits) space
public class Solution {
    public List<String> letterCombinations(String digits) {
        LinkedList<String> queue = new LinkedList<>();
        if (digits == null || digits.length() == 0) {
            return queue;
        }
        HashMap<Character, String> map = new HashMap<>();//or you can use a string array to store the vals
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        queue.add("");
        for (int i = 0; i < digits.length(); i++) {//O(K)=O(length of digits)
            while (queue.peek().length() == i) {//less than or equal to O(C^K) I guess
                String s = queue.remove();
                String letters = map.get(digits.charAt(i));
                for (int j = 0; j < letters.length(); j++) {//O(C)=O(length of mappings' string)
                    queue.add(s + letters.charAt(j));
                }
            }
        }
        return queue;
    }
}








