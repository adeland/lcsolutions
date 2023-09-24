class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        query_row += 1
        x = [poured]
        for i in range(1, query_row):
            curr = [0] * (i + 1)
            for j in range(i):
                y = x[j] - 1
                if y > 0:
                    curr[j] += .5 * y
                    curr[j + 1] += .5 * y
            x = curr
        return min(1, x[query_glass]) 
#Had assistance from Neetcodeio solution on youtube to implement solution
