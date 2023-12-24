class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {}
        x = 0
        y = 0

        for dir in path:
            curr = x, y
            if curr not in seen:
                seen[curr] = 1
            else:
                return True

            if dir == "N":
                y += 1
            elif dir == "S":
                y -= 1
            elif dir == "E":
                x -= 1
            else:
                x += 1 

        curr = x, y
        if curr in seen:
            return True
        return False

        
