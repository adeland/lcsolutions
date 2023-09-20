class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        x = 0
        while l < r:
            y = min(height[l], height[r]) * (r - l)
            x = max(x, y)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return x