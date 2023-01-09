class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        #technique -> slicing the string and store it in list then joining it by space. 
        #Use the spaces value as a slicing operator's operands 


        words = []

        words.append(s[:spaces[0]])
        spaces_size = len(spaces)

        for index in range(spaces_size - 1):
            words.append(s[spaces[index] : spaces[index + 1]])

        words.append(s[spaces[-1] : ])

        return " ".join(words)
