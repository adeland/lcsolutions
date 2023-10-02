class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            return False
        aliceMoves = 0
        bobMoves = 0
        count1 = 0
        count2 = 0
        for i in colors:
            if i == "A":
                count1 += 1
                count2 = 0
                if count1 >= 3:
                    aliceMoves += 1
            elif i == "B":
                count2 += 1
                count1 = 0
                if count2 >= 3:
                    bobMoves += 1
        return aliceMoves > bobMoves
