class Solution:
    def smallestEvenMultiple(self, n: int) -> int:  
        if n % 2 == 0:
            return n

        num = 1

        #check until the multiple of n is divided by 2
        while (n * num) % 2 != 0:
            num += 1

        return n * num
