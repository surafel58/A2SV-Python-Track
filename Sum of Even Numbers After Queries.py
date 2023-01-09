class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        #1 - first track even sum
        #2 - keep the even num index in set
        #3 - iterate query and check if the qury index is in set(), yes - subtract num[index] from even sum, No - if modified num is even add index to set and add modified val to evenSum

        evenSum = 0
        evenValIndex = set({})

        result = []

        for index, value in enumerate(nums):
            if value % 2 == 0:
                evenValIndex.add(index)
                evenSum += value

        
        for query in queries:

            if query[1] in evenValIndex:
                evenValIndex.remove(query[1])
                evenSum -= nums[query[1]]

            nums[query[1]] += query[0] 

            if nums[query[1]] % 2 == 0:
                evenValIndex.add(query[1])
                evenSum += nums[query[1]] 
            
            result.append(evenSum)

        return result
