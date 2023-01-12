class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        #store list of dictinoaries  
        dictionary_list = []
        result = []
        for word in words:
            dictionary_list.append(Counter(word))

        for value in dictionary_list[0]:
            minFreq = dictionary_list[0][value]
            for index in range(1, len(dictionary_list)):
                
                if value not in dictionary_list[index]:
                    minFreq = 0
                    break
                minFreq = min(minFreq, dictionary_list[index][value])
            
            for i in range(minFreq):
                result.append(value)

        return result
