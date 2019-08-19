
# O(max(len(l1),len(l2)))  O(max(len(l1),len(l2))+1)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i=l1
        j=l2
        dummy=ListNode(0)
        curr=dummy
        carry=0
        while i or j:
            x = i.val if i else 0
            y = j.val if j else 0
            temp = ListNode((x+y+carry)%10)
            curr.next=temp
            curr=curr.next
            carry = (x+y+carry)//10
            if i:
                i=i.next
            if j:
                j=j.next
        if carry:
            curr.next=ListNode(carry)
        return dummy.next
            
