class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res=[]
        if len(digits)==0:
            return []
        self.dfs(phone,digits,"",res)
        return res
    
    def dfs(self,phone,digits,temp,res):
        if len(digits)==0:
            res.append(temp)
            return
        d=digits[0]
        for c in phone[d]: 
            self.dfs(phone,digits[1:],temp+c,res)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        if digits:
            self.backtrack("", digits,phone,res)
        return res
    
    def backtrack(self,combination, next_digits,phone,res):
            # if there is no more digits to check
            if len(next_digits) == 0:
                res.append(combination)
                return
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    self.backtrack(combination + letter, next_digits[1:],phone,res)