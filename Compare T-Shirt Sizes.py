def compareTshirt():

    test_case = int(input())
    
    for case in range(test_case):
        
        tshirt_sizes = input().split()
        
        last_char1 = tshirt_sizes[0][-1]
        last_char2 = tshirt_sizes[1][-1]
        #check for each possibility by comparing the last chars of the inputs    
        if last_char1 != last_char2:
            if last_char1 == "S" or last_char2 == "S":
                if "S" in last_char1:
                    print("<")
                else:
                    print(">")
                    
            elif last_char1 == "L" or last_char2 == "L":
                if "L" in last_char1:
                    print(">")
                else:
                    print("<")
            
        else:
            if last_char1 == "M":
                print("=")
            
            elif last_char1 == "S":
                if len(tshirt_sizes[0]) == len(tshirt_sizes[1]):
                    print("=")
                elif len(tshirt_sizes[0]) > len(tshirt_sizes[1]):
                    print("<")
                else:
                    print(">")
            
            elif last_char1 == "L":
                if len(tshirt_sizes[0]) == len(tshirt_sizes[1]):
                    print("=")
                elif len(tshirt_sizes[0]) > len(tshirt_sizes[1]):
                    print(">")
                else:
                    print("<")
                    
compareTshirt()
