class Solution:
    def similarPairs(self, words: List[str]) -> int:
       
        #change each words to set to remove duplicate then treat them as a list and sort those words then again join them   
        words = list(map(set, words))
        words = list(map(''.join, words))
        words = list(map(sorted, words))
        words = list(map(''.join, words))
        
        #put frequency of those words
        word_freq_map = Counter(words)

        counter = 0

        for word in word_freq_map:
            word_count = word_freq_map[word]

            #formula to calculate how many possible pairs we can form for the give amount of word frequency
            counter += ((word_count * (word_count + 1)) // 2) - word_count

        return counter
