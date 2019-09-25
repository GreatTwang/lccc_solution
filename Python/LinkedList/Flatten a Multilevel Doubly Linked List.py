#   O(N)    O(number of nodes that has child)
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack=[]
        curr=head
        pre=None
        while stack or curr:
            if curr and curr.child:
                if curr.next:
                    stack.append(curr.next)
                temp=curr.child
                curr.child=None
                curr.next=temp
                temp.prev=curr
            # when reach the end of one branch and stack is not empty:
            # pop and connect
            if curr.next is None and len(stack)!=0:
                temp=stack.pop()
                curr.next=temp
                temp.prev=curr
            curr=curr.next
        return head