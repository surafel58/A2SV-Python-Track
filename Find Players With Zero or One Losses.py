class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #nlogn

        #hold only losers freq
        losersFreq = {}
        result = []

        #keep track of winners (it is a set. so as to remove duplicates)
        winner = set({})

        #keep track of losers
        loser = set({})

        #store loser - freq in dict
        for match in matches:
            if match[1] in losersFreq:
                losersFreq[match[1]] += 1
            else:
                losersFreq[match[1]] = 1

        #check if current matches winner(match[0]) is not in the dict, then we are sure that the player havent lost any math
        #check if current matches loser(match[1]) freq is 1, then  we are sure that the player have lost exactly one match
        for match in matches:
            if not(match[0] in losersFreq):
                winner.add(match[0])
            if losersFreq[match[1]] == 1:
                loser.add(match[1])

        #sort them
        result.append(sorted(list(winner)))
        result.append(sorted(list(loser)))

        return result

