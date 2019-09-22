class Solution {
    List<List<Integer>> res=new ArrayList<>();
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        int level=0;
        if(root==null) return res;
        q.add(root);
        while(!q.isEmpty()){
            int size=q.size();
            res.add(new LinkedList<Integer>());
            for(int i=0;i<size;i++){
                TreeNode cur=q.remove();
                if(level%2==0)
                    res.get(level).add(cur.val);
                else ((LinkedList)res.get(level)).addFirst(cur.val);
                if(cur.left!=null) q.add(cur.left);
                if(cur.right!=null) q.add(cur.right);
            }
            level++;
            
        }
        return res;
    }
}







