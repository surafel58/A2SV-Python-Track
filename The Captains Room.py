# Enter your code here. Read input from STDIN. Print output to STDOUT
#
k = int(input())
room_list = input().split()

roomMap = {}

for room in room_list:
  if room in roomMap:
    roomMap[room] += 1
  else:
    roomMap[room] = 1
    
for room in roomMap:
  if roomMap[room] == 1:
    print(room) 
