# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

grpA_size, grpB_size = list(map(int, input().split()))

grpA = []
grpB = []

for num in range(grpA_size):
  grpA.append(input())
  
for num in range(grpB_size):
  grpB.append(input())

#initialize a default dict with list
grpA_char_occur = defaultdict(list)

#for each char in group A, append the current characters index + 1 to a list, which is a value of current char key
for index in range(grpA_size):
  grpA_char_occur[grpA[index]].append(str(index + 1))
  
#join the list with space and print it, print -1 if dict returns [] 
for word in grpB:
  occurence = ' '.join(grpA_char_occur[word])
  if len(occurence) == 0:
    print(-1)
  else:
    print(occurence)
