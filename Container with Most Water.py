class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr_area = 0
        max_area = 0

        while l < r:
            curr_area = (r - l) * min(height[l], height[r])
            if curr_area > max_area:
                max_area = curr_area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
                
        return max_area
