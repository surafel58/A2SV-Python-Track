class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        #smallest distance index and minimum distance so far
        smallestDistIndex = -1
        mindistance = 2**31 - 1

        #iterate through the list and keep track of the minimum M distance and the index of those points 
        for index, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance = abs(x - point[0]) + abs(y - point[1])
                if distance < mindistance:
                    mindistance = distance
                    smallestDistIndex = index

        #check if the index is changed, then valid point found and return the index
        if smallestDistIndex != -1:
            return smallestDistIndex

        #otherwise return -1
        return -1        
        
