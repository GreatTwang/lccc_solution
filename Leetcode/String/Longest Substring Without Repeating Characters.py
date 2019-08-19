# O(n)   O(1)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charmap =dict()
        left = 0
        longest = 0
        right = 0
        for c in s:
            if c in charmap and charmap[c]>=left:
                left=charmap[c]+1
            charmap[c]=right
            curr_length = right-left+1
            if curr_length>longest:
                longest=curr_length
            right+=1
        return longest