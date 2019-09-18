# O(max(len(l1),len(l2)))  O(max(len(l1),len(l2))+1))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = list()
        stack2 = list()
        while l1:
            stack1.append(l1)
            l1=l1.next
        while l2:
            stack2.append(l2)
            l2=l2.next
        carry=0
        curr=None
        while len(stack1) or len(stack2):
            x=stack1.pop().val if len(stack1) else 0
            y=stack2.pop().val if len(stack2) else 0
            digit=(x+y+carry)%10
            carry=(x+y+carry)//10
            new=ListNode(digit)
            new.next=curr
            curr=new
        if carry:
            new=ListNode(carry)
            new.next=curr
            curr=new
        return curr
 