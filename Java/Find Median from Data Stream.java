//2 Priorityqueue   O(log(N))   O(N)   
class MedianFinder {
    PriorityQueue<Integer> lo;
    PriorityQueue<Integer> hi;

    /** initialize your data structure here. */
    public MedianFinder() {
        lo = new PriorityQueue<>(new Comparator<Integer>() {
        @Override
        public int compare(Integer a1, Integer a2) {
            return a2 - a1;
        }
        });
        
        hi = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        lo.offer(num);
        hi.offer(lo.peek());
        lo.poll();
        if(lo.size() < hi.size()) {
            lo.offer(hi.peek());
            hi.poll();
        }
    }
    
    public double findMedian() {
        return lo.size() > hi.size() ? (double) lo.peek() : (lo.peek() + hi.peek())*0.5;
    }
}









