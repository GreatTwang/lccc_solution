class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy_new = Node(None, None, None)
        mappings = dict()
    
        old_node = head
        prev_new = dummy_new
        while old_node:
            new_node = Node(old_node.val, None, None)
            mappings[id(old_node)] = new_node
            prev_new.next = new_node
            prev_new = new_node
            old_node = old_node.next  
            
        old_node = head
        new_node = dummy_new.next
        while old_node:
            if old_node.random == None:
                new_node.random = None
            else:
                new_node.random = mappings[id(old_node.random)]
            old_node = old_node.next
            new_node = new_node.next
    
        return dummy_new.next