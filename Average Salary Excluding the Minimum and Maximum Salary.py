class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary)
        sum = 0
        for index in range(1, n - 1):
            sum += salary[index]
        
        avg = sum/(n - 2) 
        return avg
