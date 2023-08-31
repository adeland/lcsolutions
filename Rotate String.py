class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        goal = list(goal)
        x = s
        for i in s:
            x.append(i)
            x = x[1:]
            if x == goal:
                return True
        return False
