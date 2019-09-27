class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mylist = []
        curr = head
        while curr != None:
            mylist.append(curr.val)
            curr = curr.next
        mylist.sort()
        curr = head
        for i in range(len(mylist)):
            curr.val = mylist[i]
            curr = curr.next
        return head
            