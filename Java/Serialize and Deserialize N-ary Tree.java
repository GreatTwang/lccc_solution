// queue O(N) O(N)
class Codec {
    // still use level order
    // Encodes a tree to a single string.
    public String serialize(Node root) {
        if (root == null)   return null;
        StringBuilder sb = new StringBuilder();
        Queue<Node> queue = new LinkedList<>();
        sb.append(root.val);
        sb.append("#");
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Node curr = queue.poll();
                if (curr != null) {
                    List<Node> children = curr.children;
                    if (children == null || children.size() == 0) {
                        sb.append("null");
                    } else {
                        for (Node c : children) {
                            sb.append(c.val);
                            sb.append(",");
                            queue.offer(c);
                        }
                    }
                    sb.append("#");
                }
            }
        }
     //   System.out.println(sb.toString());
        return sb.toString().substring(0, sb.length() - 1);
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if (data == null)   return null;
        Queue<Node> parents = new LinkedList<>();
        String[] elements = data.split("#");
        Node root = new Node(Integer.valueOf(elements[0]), null);
        parents.offer(root);
        for (int i = 1; i < elements.length; i++) {
            Node parent = parents.poll();
            String[] kids = elements[i].split(",");
            List<Node> c = new ArrayList<>();
            for (String kid : kids) {
                if (kid.length() == 0)  continue;
                if (kid.equals("null")) continue;
                Node k = new Node(Integer.valueOf(kid), null);
                c.add(k);
                parents.offer(k);
            }
            parent.children = c;
        }
        return root;
    }
}














