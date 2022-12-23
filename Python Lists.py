def insertElement(input_list, i, e):
  input_list.insert(i, e)

def removeElement(input_list, e):
  input_list.remove(e)

def appendElement(input_list, e):
  input_list.append(e)

def sortList(input_list):
  input_list.sort()

def popElement(input_list):
  input_list.pop()

def reverseList(input_list):
  input_list.reverse()

def printList(input_list):
  print(input_list)

if __name__ == '__main__':
    N = int(input())
    input_list = []
    
    for n in range(N):
      command = input().split(" ")
      
      if command[0] == 'insert':
        insertElement(input_list, int(command[1]), int(command[2]))
      
      elif command[0] == 'reverse':
        reverseList(input_list)
        
      elif command[0] == 'remove':
        removeElement(input_list, int(command[1]))
      
      elif command[0] == 'append':
        appendElement(input_list, int(command[1]))
      
      elif command[0] == 'sort':
        sortList(input_list)
      
      elif command[0] == 'pop':
        popElement(input_list)
      
      else:
        printList(input_list)
      
