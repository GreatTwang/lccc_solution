class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        pre=Node(0,None,None,None)    
        pre.next=head
        curr=head
        stack=[]
        while stack or curr:
            if curr is None:
                curr=stack.pop()
            if curr.child:
                pre.next=curr
                if pre.next!=head:
                    curr.prev=pre
                pre=curr
                if curr.next:
                    stack.append(curr.next)
                temp=curr.child
                curr.child=None
                curr=temp
            else:
                pre.next=curr
                if pre.next!=head:
                    curr.prev=pre
                pre=curr
                curr=curr.next
        return head