class Solution {
    public int myAtoi(String str) {
        
        if(str == null || str.trim().length() == 0 || str.length() == 0) return 0;
        str = str.trim();
        char first = str.charAt(0);
        int sign = 1, start = 0;
        long sum = 0;
        if(first == '-') {
            sign = -1;
            start++;
        }
        if(first == '+') {
            sign = 1;
            start++; 
        }
        
        for(int i = start; i < str.length(); i++) {
            if(!Character.isDigit(str.charAt(i))) {
                return (int) sum * sign;
                }
            sum = sum * 10 + (str.charAt(i) - '0');
            if(sign == 1 && sum > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            if(sign == -1 && (-1) * sum < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
        }
        return (int) sum*sign;
        
    }
}










