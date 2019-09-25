class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step = 1, 1
        right = True
        while n > 1:
            if right or n%2 == 1:
                head += step
            step *= 2
            n >>= 1
            right = not right
        return head