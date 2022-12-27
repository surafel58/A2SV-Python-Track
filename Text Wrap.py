import textwrap

def wrap(string, max_width): 
    result = []
    n = len(string)
    wrapped_text = [] 
    index = 0
    
    while index < n:
      
      wrapped_text.append(string[index])
      
      if (index + 1) % max_width == 0:
        wrapped_text = ''.join(wrapped_text)
        result.append(wrapped_text)
        wrapped_text = []
        
      index += 1
      
    wrapped_text = ''.join(wrapped_text)
    result.append(wrapped_text)
      
    return '\n'.join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
