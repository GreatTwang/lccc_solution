class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next
        root=self.helper(lst,0,len(lst)-1)
        return root
    def helper(self,nums,l,r):
        if l>r:
            return None
        if l==r:
            return TreeNode(nums[l])
        mid=(l+r)//2
        node=TreeNode(nums[mid])
        node.left=self.helper(nums,l,mid-1)
        node.right=self.helper(nums,mid+1,r)
        return node