//stacks of stacks     https://leetcode.com/problems/maximum-frequency-stack/solution/
class FreqStack {
    Map<Integer, Integer> freq;
    Map<Integer, Stack<Integer>> group;
    int maxfreq;

    public FreqStack() {
        freq = new HashMap();
        group = new HashMap();
        maxfreq = 0;
    }

    public void push(int x) {  //O(1)
        int f = freq.getOrDefault(x, 0) + 1;
        freq.put(x, f);
        if (f > maxfreq)
            maxfreq = f;
        group.computeIfAbsent(f, z-> new Stack()).push(x);
    }

    public int pop() {  //O(1)
        int x = group.get(maxfreq).pop();
        freq.put(x, freq.get(x) - 1);
        if (group.get(maxfreq).size() == 0)
            maxfreq--;
        return x;
    }
}















