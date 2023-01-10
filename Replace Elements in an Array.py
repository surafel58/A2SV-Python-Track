class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
  
        num_index_map = {}

        #store value - index in dict
        for index, num in enumerate(nums):
            num_index_map[num] = index
        
        for operation in operations:
            #store the index of the number to be modified
            index = num_index_map[operation[0]]

            #assign the new number to that index
            nums[index] = operation[1]
            
            #remove the old value from the dict and add a new key value pair (new value - curr index) 
            num_index_map.pop(operation[0])
            num_index_map[operation[1]] = index 
            

        return nums
