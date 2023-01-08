class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        #conditions
        #true - a[i] < b[i] => break
        #false - a[i] > b[i], len(a) > len(b) => return False

        order_map = {}

        #give each char in order str a value 
        for value, char in enumerate(order):
            order_map[char] = value 

        words_size = len(words)

        for index in range(words_size - 1):
           #store the current and the next word len
            word1_size = len(words[index])
            word2_size = len(words[index + 1])
            
            #compare each char of curr and next word, and check the above conditions
            for index2 in range(min(word1_size, word2_size)):
                char1 = words[index][index2]
                char2 = words[index + 1][index2]
                print(char1, char2)
                
                if order_map[char1] > order_map[char2]:
                    return False
                
                elif order_map[char1] < order_map[char2]:
                    break

            else:
                if word1_size > word2_size:
                    return False

        return True
