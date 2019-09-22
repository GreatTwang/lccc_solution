class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        HashMap<Character, Integer> map = new HashMap<>();
        List<Integer> res = new LinkedList<>();
        for(char c : p.toCharArray()) {
            map.put(c, map.getOrDefault(c, 0)+1);
        }
        int size = map.size();
        int l = 0, r = 0;
        while(r < s.length()) {
            char t = s.charAt(r);
            if(map.containsKey(t)) {
                map.put(t, map.get(t)-1);
                if(map.get(t) == 0) {size--;}
            }
            r++;           
             while(size == 0) {
                 char temp = s.charAt(l);
                 if(map.containsKey(temp)) {
                     map.put(temp, map.get(temp)+1);
                     if(map.get(temp) > 0) {size++;}  
                 }
                 if(r -l == p.length()) {res.add(l);}
                 l++;
             }
            }
        return res;
    }
}








