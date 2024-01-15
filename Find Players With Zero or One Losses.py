class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = {}
        
        for match in matches:
            if match[0] not in players:
                players[match[0]] = 0
            if match[1] not in players:
                players[match[1]] = 1
            else:
                players[match[1]] += 1

        ret = []
        ret2 = []

        for score in players:
            if players.get(score) == 0:
                ret.append(score)
            if players.get(score) == 1:
                ret2.append(score)

        ret.sort()
        ret2.sort()

        return [ret, ret2]    
