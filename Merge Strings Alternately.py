class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #result list
        altr_str = []

        #index
        index = 0

        #append the char alternatively
        while index < min(len(word1), len(word2)):
            altr_str.append(word1[index])
            altr_str.append(word2[index])
            index += 1

        #append the remaning characters
        while index < len(word1):
            altr_str.append(word1[index])
            index += 1

        while index < len(word2):
            altr_str.append(word2[index])
            index += 1

        
        #return the string result
        return "".join(altr_str)    
