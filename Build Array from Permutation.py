class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        nums_size = len(nums)
        ans = [0] * nums_size
        
        for index in range(nums_size):
            ans[index] = nums[nums[index]]
        
        return ans
