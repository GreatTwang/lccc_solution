class Solution:
    def compress(self, chars: List[str]) -> int:
        c_end = 0
        digit_end = 0
        for i, c in enumerate(chars):
            if i == len(chars)-1 or chars[i + 1] != c:
                chars[digit_end] = chars[c_end]
                digit_end += 1
                if i > c_end:
                    for digit in str(i - c_end + 1):
                        chars[digit_end] = digit
                        digit_end += 1
                c_end = i + 1
        return digit_end