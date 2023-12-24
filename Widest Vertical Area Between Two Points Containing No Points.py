class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        x = []
        ret = 0

        for elements in points:
            x.append(elements[0])

        for point in range(len(x)):
            if point == len(x) - 1:
                break
            check = x[point + 1] - x[point]
            ret = max(ret, check)

        return ret
