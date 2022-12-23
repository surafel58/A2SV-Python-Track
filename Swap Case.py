def swap_case(s):
  result = ""
  
  #change lower chaar to upper and vice versa then append it to the result string
  for char in s:
    if(char.islower()):
      result = result + char.upper()
      
    else:
      result = result + char.lower()
      
  return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
