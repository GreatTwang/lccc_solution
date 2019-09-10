public class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int index = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[index--] = nums1[i--];
            } else {
                nums1[index--] = nums2[j--];
            }
        }
        while (j >= 0) {
            nums1[index--] = nums2[j--];
        }
    }
}
//if we start to fill nums1 from the front, the original values of nums1 may be changed before we put them into a correct pos
//so we start from back(index) of nums1, even if all nums in nums2 are larger than nums1, values in nums won't get messed up


// iterator for 2 sorted arrays' iterators: O(n + m) time, O(1) space
public class iteratorForTwoSortedArrays {
    /**
     * @param arrays k sorted integer arrays
     * @return a sorted array
     */
    public class ArrayIterator {
        Integer val;//use val to store the next value of this array
        Iterator it;//store this array's iterator
        public ArrayIterator(Iterator i) {
            val = i.next();
            it = i;
        }
    }
    
    private ArrayIterator it_a;
    private ArrayIterator it_b;
    
    public iteratorForTwoSortedArrays(Iterator a, Iterator b) {
        if (a.hasNext()) {
            it_a = new ArrayIterator(a);
        }
        if (b.hasNext()) {
            it_b = new ArrayIterator(b);
        }
    }
    
    public int next() {//assume next() will be called only if hasNext() is true
        if (it_a.val == null) {
            return helper(it_b);
        }
        if (it_b.val == null) {
            return helper(it_a);
        }
        //if both of them are not null
        if (it_a.val <= it_b.val) {
            return helper(it_a);
        } else {
            return helper(it_b);
        }
    }

    public boolean hasNext() {
        return it_a.val != null || it_b.val != null;
    }
    
    private int helper(ArrayIterator curr) {
        int res = curr.val;
        if (curr.it.hasNext()) {
            curr.val = it.next();
        } else {
            curr.val = null;
        }
        return res;
    }
}









