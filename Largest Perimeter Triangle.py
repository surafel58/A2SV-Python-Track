class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums_size = len(nums)
        max_perimeter = 0

        #sort the elements to get the largest perimeter of valid triangle
        nums.sort()
        for index in range(2, nums_size):
            #side of triangle
            a = nums[index]
            b = nums[index - 1]
            c = nums[index - 2]

            #check validity of given side length and calculate the perimeter and store the max perimeter
            if a + b > c and a + c > b and b + c > a:
                max_perimeter = max(max_perimeter, a + b + c)
        
        return max_perimeter
