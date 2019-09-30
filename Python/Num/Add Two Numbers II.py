# O(max(len(l1),len(l2)))  O(len(l1)+len(l2))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1=[]
        stack2=[]
        # save values of l1,l2 to stack1 stack2
        p1=l1
        p2=l2
        while(p1):
            stack1.append(p1.val)
            p1=p1.next
        while(p2):
            stack2.append(p2.val)
            p2=p2.next
        # start from the top of two stacks
        carry=0
        curr=None
        while stack1 or stack2:
            x=stack1.pop() if stack1 else 0
            y=stack2.pop() if stack2 else 0
            z=(x+y+carry)%10
            carry=(x+y+carry)//10
            # create new node for current digit; add from the front
            node=ListNode(z)
            node.next=curr
            curr=node
        #if carry is not 0 at last
        if carry:
            node=ListNode(carry)
            node.next=curr
            curr=node
        return curr
 