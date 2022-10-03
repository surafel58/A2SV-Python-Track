if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    # sort list
    scores.sort()
    
    # store maximum value from list
    maxVal = scores[n-1]
    
    # remove the first maximum element
    scores.pop(n-1)
    
    # keep removing the maximum element until you find the second max element
    while maxVal == scores[len(scores) - 1]:
      scores.pop(len(scores) - 1)
      
    # print the second max element
    print(scores[len(scores) - 1])
