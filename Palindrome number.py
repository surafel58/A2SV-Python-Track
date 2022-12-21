class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x < 10:
            return True
        
        reverse_num = 0
        
        #quoteint - result divided by 10, rem - reminder of quotient divided by 10, i = tenth place counter
        quotient = x
        rem = 0
        i=1
        
        #start i from the last digit place
        i = int(math.pow(10, len(str(x)) - 1))
        
        #keep dividing the quotient and reverse the number 
        while quotient != 0:
            rem = quotient % 10
            quotient //= 10
            reverse_num += rem*i
            i //= 10

         #if the reversed number is the same, return true
        if reverse_num == x:
            return True
            
        #otherwise, false
        return False
