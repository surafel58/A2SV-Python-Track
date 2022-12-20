# Enter your code here. Read input from STDIN. Print output to STDOUT
length = input().split()
n = int(length[0])
m = int(length[0])

hapiness = 0

elements = input().split()

A = set(input().split())
B = set(input().split())

for i in range(m):
  if elements[i] in A:
    hapiness += 1
  elif elements[i] in B:
    hapiness -= 1
    
print(hapiness)
