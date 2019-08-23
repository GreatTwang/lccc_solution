class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:
            mid = low + ((high - low) // 2)
            guess_ = guess(mid)

            if guess_ == 0:
                return mid
            if guess_ < 0:
                high = mid - 1
            elif guess_ > 0:
                low = mid + 1