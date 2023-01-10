class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        visited = set({})
        m = len(matrix)
        n = len(matrix[0])

        right = True
        down = False
        left = False
        up = False

        i = 0
        j = 0

        #simulate the process until all elements are found or visited
        while len(visited) != (n*m):
            currIndex = str(i) + str(j)
            
            while right and j < n and currIndex not in visited:
                
                visited.add(currIndex)
                result.append(matrix[i][j])
                j += 1 
                currIndex = str(i) + str(j)
            
            
            j -= 1
            i += 1
            down = True
            right = False

            currIndex = str(i) + str(j)
            while down and i < m and currIndex not in visited:
                # currIndex = str(i) + str(j)
                visited.add(currIndex)
                result.append(matrix[i][j])
                i += 1 
                currIndex = str(i) + str(j)
            
            
            i -= 1
            j -= 1
            left = True
            down = False


            currIndex = str(i) + str(j)
            while left and j >= 0 and currIndex not in visited:
                visited.add(currIndex)
                result.append(matrix[i][j])
                j -= 1 
                currIndex = str(i) + str(j)

            
            j += 1
            i -= 1
            up = True
            left = False
            

            currIndex = str(i) + str(j)
            while up and i >= 0 and currIndex not in visited:
                visited.add(currIndex)
                result.append(matrix[i][j])
                i -= 1 
                currIndex = str(i) + str(j)
            
          
            i += 1
            j += 1
            right = True
            up = False

        return result
