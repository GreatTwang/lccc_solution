//Input: version1 = "1.01", version2 = "1.001"      Output: 0
//
class Solution {
    public int compareVersion(String version1, String version2) {
        int t1 = 0, t2 = 0;
        int p1 = 0, p2 = 0;
        while(p1 < version1.length() || p2 < version2.length()) {
            while(p1 < version1.length() && version1.charAt(p1) != '.') {
                t1 = t1 * 10 + version1.charAt(p1) - '0'; 
                p1++;
            }
            while(p2 < version2.length() && version2.charAt(p2) != '.') {
                t2 = t2 * 10 + version2.charAt(p2) - '0';
                p2++;
            }
            if(t1 != t2) return t1 > t2 ? 1 : -1;
            t1 = 0; t2 = 0;
            p1++; p2++;
        }
        return 0;
    }
}