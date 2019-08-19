#    O(m+n)    O(max(m,n))
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeset=set()
        while headA:
            nodeset.add(headA)
            headA=headA.next
        while headB:
            if headB in nodeset:
                return headB
            headB=headB.next
        return None
#   better method  O(m+n)   O(1)     
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa is not pb:
            pa = pa.next if pa is not None else headB
            pb = pb.next if pb is not None else headA
        return pa

            