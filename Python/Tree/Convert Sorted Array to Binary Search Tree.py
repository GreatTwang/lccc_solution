#   O(N)    O(1)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root=self.helper(nums,0,len(nums)-1)
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