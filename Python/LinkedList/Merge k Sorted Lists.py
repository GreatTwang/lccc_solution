class Solution:
    # recursive
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        mid = len(lists)//2
        res = self.mergeTwoLists(self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:]))
        return res

    # iterative     O(Nlog k)    O(1)
    def mergeKLists(self, lists):
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next
            else: 
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1:
            curr.next=l1
        else:
            curr.next=l2
        return dummy.next