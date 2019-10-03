class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            temp=slow.next
            slow.next = rev    
            rev = slow
            slow = temp
        # CHECK odd
        if fast:
            slow = slow.next
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True