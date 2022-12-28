class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        #formula for finding how many pairs exist in an array given their frequency
        # e.g - a : 3, n(n+1)/2 - n
        
        total = 0
        freq_map = Counter(nums)
        for freq in freq_map:
            n = freq_map[freq]
            total += ((n*(n+1)//2) - n)

        return total
