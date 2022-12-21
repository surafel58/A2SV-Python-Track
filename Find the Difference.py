class Solution:
    def findTheDifference(self, s: str, t: str) -> str:


        s_freq = {}
        t_freq = {}

        for char in s:
            if char in s_freq:
                s_freq[char] += 1
            else:
                s_freq[char] = 0 

        for char in t:
            if char in t_freq:
                t_freq[char] += 1
            else:
                t_freq[char] = 0

        for char in t:
            if not(char in s_freq) or (s_freq[char] != t_freq[char]):
                return char

        return ""
