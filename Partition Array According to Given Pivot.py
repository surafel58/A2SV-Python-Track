class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        #used a key function that returns 1, -1, 0 and sort them based on the pivot
        #return -1 - if value < pivot: 
        #return 1 -  if value > pivot:
        #return 0 - if value == pivot
        def keyFunc(value: int) -> int:
            if value < pivot:
                return -1
            elif value > pivot:
                return 1

            return 0

        nums.sort(key=keyFunc)

        return nums
