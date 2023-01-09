class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive_list = []
        negative_list = []

        result = [0] * len(nums)
        nums_size = len(nums)
        
        
        for num in nums:
            if num > 0:
                positive_list.append(num)
            else:
                negative_list.append(num)

        index2 = 0
        positive_list_size = len(positive_list)

        for index in range(0, nums_size, 2):
            if index2 >= positive_list_size:
                break 

            result[index] = positive_list[index2]
            index2 += 1

        index2 = 0
       
        for index in range(1, nums_size, 2):
            if index2 >= positive_list_size:
                break
            result[index] = negative_list[index2]
            index2 += 1

        return result
        
