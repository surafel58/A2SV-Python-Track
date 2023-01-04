class Solution:
    def freqAlphabets(self, s: str) -> str: 
        
        str_size = len(s)
        counter = 0
        flag = False
        temp = ""
        result = ""
        # start from last char and store 2 digits whenever # is found
        for index in range(str_size - 1, -1, -1):
            if s[index] == "#":
                flag = True
                continue
            
            if not flag:
                #calculate letter offset
                letter = 97 - 1 + int(s[index])
                result = chr(letter) + result
            #store 2 digits
            else:
                counter += 1
                temp = s[index] + temp

                if counter == 2:
                    flag = False
                    letter = 97 - 1 + int(temp)
                    result = chr(letter) + result
                    temp = ""
                    counter = 0
                
        return result

