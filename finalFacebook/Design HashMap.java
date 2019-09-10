//no resize   separate chaining
class MyHashMap {
        final ListNode[] nodes = new ListNode[10000];
        
    class ListNode {
            int key, val;
            ListNode next;

            ListNode(int key, int val) {
                this.key = key;
                this.val = val;
            }
        }
    
        public void put(int key, int value) {
            int i = idx(key);
            if (nodes[i] == null)
                nodes[i] = new ListNode(-1, -1);
            ListNode prev = find(nodes[i], key);
            if (prev.next == null)
                prev.next = new ListNode(key, value);
            else prev.next.val = value;
        }

        public int get(int key) {
            int i = idx(key);
            if (nodes[i] == null)
                return -1;
            ListNode node = find(nodes[i], key);
            return node.next == null ? -1 : node.next.val;
        }

        public void remove(int key) {
            int i = idx(key);
            if (nodes[i] == null) return;
            ListNode prev = find(nodes[i], key);
            if (prev.next == null) return;
            prev.next = prev.next.next;
        }

        int idx(int key) { return Integer.hashCode(key) % nodes.length;}

        ListNode find(ListNode bucket, int key) {
            ListNode node = bucket, prev = null;
            while (node != null && node.key != key) {
                prev = node;
                node = node.next;
            }
            return prev;
        }


    }

//resizable   open addressing
class MyHashMap {
    private class Entry {
        public int key;
        public int value;
        public Entry(int key, int value) {
            this.key = key;
            this.value = value;            
        }
    }
    
    private static int PAGE_SIZE = 16;
    private static float LOAD_FACTOR = 0.75f;
    private int numPages = 1;
    private int itemCount = 0;
    private List<LinkedList<Entry>> map;     
    
    /** Initialize your data structure here. */
    public MyHashMap() {
        map = new ArrayList<>(PAGE_SIZE);
        for (int i = 0; i < PAGE_SIZE; i++) {
            map.add(null);
        }
    }
    
    /** value will always be non-negative. */
    public void put(int key, int value) {
        //compute hash
        int hash = computeHash(key);        
        //check if exists
        Entry prevEntry = getEntry(key);
        if (prevEntry != null) {
            prevEntry.value = value;
            return;
        }
        //Resize first so we don't add this entry twice        
        if (reachedCapacity(1)) {
            //System.out.println("reachedCapacity=" + itemCount);
            rehash();
        }        
        //add to list
        hash = computeHash(key);
        LinkedList ll = map.get(hash);
        if (ll == null) {
            ll = new LinkedList<Entry>();
            map.set(hash, ll);
        }            
        ll.add(new Entry(key, value));
        itemCount++;
    }
    
    private void rehash() {
        List<LinkedList<Entry>> tempTable = map;
        numPages = numPages * 2; //double size
        int newSize = numPages * PAGE_SIZE;
        itemCount = 0;  //map is empty now
        //init new map
        map = new ArrayList<>(newSize);
        for (int i = 0; i < newSize; i++) {
            map.add(null);
        }
        //add old items
        for (LinkedList<Entry> ll : tempTable) {
            if (ll != null) {
                for (Entry entry : ll) {
                    this.put(entry.key, entry.value);
                }
            }
        }









