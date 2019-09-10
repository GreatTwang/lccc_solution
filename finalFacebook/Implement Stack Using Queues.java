//2 queue   O(n)  O(1)
class MyStack {
    private Queue<Integer> q1 = new LinkedList<>();
    private Queue<Integer> q2 = new LinkedList<>();
    private int top;
    /** Initialize your data structure here. */
    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {  //O(n)
        q2.add(x);
        top = x;
        while (!q1.isEmpty()) {                
            q2.add(q1.remove());
        }
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int temp = q1.remove();
        if (!q1.isEmpty()) {
            top = q1.peek();
        }
        return temp;
    }
    
    /** Get the top element. */
    public int top() {
        return top;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return q1.isEmpty();
    }
}

//1 queue
class MyStack {
    private LinkedList<Integer> q1 = new LinkedList<>();
    /** Initialize your data structure here. */
    public MyStack() {

    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        q1.add(x);
        int sz = q1.size();
        while (sz > 1) {
            q1.add(q1.remove());
            sz--;
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int temp = q1.remove();
        return temp;
    }
    
    /** Get the top element. */
    public boolean empty() {
        return q1.isEmpty();
    }
    
    /** Returns whether the stack is empty. */
    public int top() {
        return q1.peek();
    }
}









