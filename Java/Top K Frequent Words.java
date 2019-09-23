// O(Nlog(k))   O(N)
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> res = new LinkedList<>();
        HashMap<String, Integer> map = new HashMap<>();
        for(String word: words) {
            map.put(word, map.getOrDefault(word, 0)+1);
        }
        PriorityQueue<String> q = new PriorityQueue<>(new Comparator<String>() {
            @Override
            public int compare(String a1, String a2) {
                return (map.get(a1).equals(map.get(a2)) ? a2.compareTo(a1) : map.get(a1) - map.get(a2));
            }
        });
        
        for(String word : map.keySet()) {
            q.offer(word);
            if(q.size() > k) {
                q.poll();
            }
        }
        while(!q.isEmpty()) {
            res.add(q.poll());
        }
        Collections.reverse(res);
        return res;
    }
}













