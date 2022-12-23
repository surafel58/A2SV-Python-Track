# Enter your code here. Read input from STDIN. Print output to STDOUT
setA = set(map(int, input().split()))
n = int(input())

setList = []
isStrictSuperSet = True

for i in range(n):
  currentSet = set(map(int, input().split()))
  setList.append(currentSet)
  
for currentSet in setList:
  #check if set A is not super set of each set or len of setA <= current Set 
  if not setA.issuperset(currentSet) or len(setA) <= len(currentSet):
    isStrictSuperSet = False
    break

if isStrictSuperSet:
  print(True)
  
else:
  print(False)
