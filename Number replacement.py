def isNumReplacementValid():

    test_case = int(input())
    for case in range(test_case):
        input_size = int(input())
        numList = input().split()
        string = input()

        #num - string map dictionary
        num_char_map = {}

        #for each number check if its mapped with character or not, if it doesn't map then map it, 
        # else check if the char mapped with the num is equal to the current char in string or not  
        for index in range(input_size):
            if numList[index] in num_char_map:
                if num_char_map[numList[index]] != string[index]:
                    print("NO")
                    break
            else:
                num_char_map[numList[index]] = string[index]
        else:
            print("YES")

isNumReplacementValid()
