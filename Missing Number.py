class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsMap = {}
        for i, val in enumerate(nums):
            numsMap[val] = i 

        for i in range(len(nums) + 1):
            if not (i in numsMap):
                return i 


        return len(numsMap)
