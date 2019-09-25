#   O(N)    O(1)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        # Creating a new weaved list of original and copied nodes.
        # If A->B->C then A->A'->B->B'->C->C'
        curr = head
        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        # use the original nodes' random pointers to assign references to random pointers for cloned nodes
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        # split original and cloned nodes
        old = head # A->B->C
        new = head.next # A'->B'->C'
        dummy = head.next
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            old = old.next
            new = new.next
        return dummy
#   O(N)    O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #table stores old-new pairs
        table={}
        dummy=Node(None,None,None)
        pre=dummy
        old=head
        while old:
            temp = Node(old.val,None,None)
            table[old]=temp
            pre.next=temp
            pre=temp    #not old!!
            old=old.next
        old=head
        new=dummy.next
        i=0
        while old:
            if old.random==None:
                new.random=None
            else:
                new.random=table[old.random]
            new=new.next
            old=old.next
        return dummy.next