class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left == 0:
                    right += 1
                else:
                    left -= 1

        def dfs(depth, left, right, left_rem, right_rem, cur):
            if depth == len(s):
                if left == right and left_rem == right_rem == 0:
                    self.ans.add(cur)
                    return
            else:  # s[depth] can only be either a left paren, right paren or a letter
                if s[depth] == "(":
                    if left_rem > 0:   # if we can remove a left paren
                        dfs(depth + 1, left, right, left_rem - 1, right_rem, cur)
                    dfs(depth + 1, left + 1, right, left_rem, right_rem, cur + "(")  # keep current left paren
                elif s[depth] == ")":
                    if right_rem > 0:  # if we can remove a right paren
                        dfs(depth + 1, left, right, left_rem, right_rem - 1, cur)
                    if left > right:  # if we can keep the right paren, see LC 22. Generate Parentheses
                        dfs(depth + 1, left, right + 1, left_rem, right_rem, cur + ")")
                else:  
                    dfs(depth + 1, left, right, left_rem, right_rem, cur + s[depth])  # we must keep the letter

        self.ans = set()
        dfs(0, 0, 0, left, right, "")
        return list(self.ans)



