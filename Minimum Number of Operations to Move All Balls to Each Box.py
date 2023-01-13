class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #122
        #210

        leftSum = [0] * len(boxes)
        rightSum = [0] * len(boxes)
        result = [0] * len(boxes)
        count = 0

        if boxes[0] == "1":
            count += 1
        
        for index in range(1, len(boxes)):
            leftSum[index] = count + leftSum[index - 1]
            if boxes[index] == "1":
                count += 1
            

        count = 0
        if boxes[-1] == "1":
            count = 1

        for index in range(len(boxes) - 2, -1, -1):
            rightSum[index] = count + rightSum[index + 1]
            if boxes[index] == "1":
                count += 1

        for index in range(len(boxes)):
            result[index] = rightSum[index] + leftSum[index]

        return result
