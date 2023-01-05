class Solution:
    def printVertically(self, s: str) -> List[str]:
        #max
        word_list = s.split()
        len_max = 0
        
        for word in word_list:
            len_max = max(len_max, len(word))

        result = [""] * len_max

        for word in word_list:
            for index in range(len_max):
                if index < len(word):
                    result[index] += word[index]
                else:
                    result[index] += " "
        
        for index in range(len_max):
            result[index] = result[index].rstrip()
        return result
