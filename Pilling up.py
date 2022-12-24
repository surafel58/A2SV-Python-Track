# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
cubes = []
for testcase in range(T):
  n = int(input())
  cubes.append(list(map(int, input().split())))


for cube in cubes:
  pile = []

  left = 0
  right = len(cube) - 1

  if cube[left] >= cube[right]:
    pile.append(cube[left])
    left += 1

  else:
    pile.append(cube[right])
    right -= 1 

  while left < right:
    if cube[left] <= pile[-1] and cube[right] <= pile[-1]:
      
      if cube[left] >= cube[right]:
        pile.append(cube[left])
        left += 1
        
      else:
        pile.append(cube[right]) 
        right -= 1  
    else:
      break
    
  if left != right:
    print('No')
    
  else:
    print('Yes')
