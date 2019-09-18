class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0 :
            return "Zero"
        
        LESS_THAN_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]
        
        def helper(n) :
            if n == 0 :
                return ""
            if n < 20 :
                return LESS_THAN_TWENTY[n] + " "
            elif n < 100 :
                return TENS[n//10] + " " + helper(n%10)
            else :
                return LESS_THAN_TWENTY[n//100] + " Hundred " + helper(n%100)
        
        res, i = "", 0
        while num > 0 :
            if num % 1000 != 0 :
                res = helper(num%1000) + THOUSANDS[i] + " " + res
            i += 1
            num //= 1000
        return res.strip()