class Solution:
    def dailyTemperatures(self, temperatures):
        ret = [0] * len(temperatures)
        stack = []

        for i, j in enumerate(temperatures):
            while len(stack) != 0 and j > stack [-1][0]:
                temp, temp2 = stack.pop()
                ret[temp2] = i - temp2
            stack.append([j,i])
        
        return ret

#NOT MY SOLUTION
