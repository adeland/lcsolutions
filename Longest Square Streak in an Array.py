class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        counts = set(nums)
        max_streak = 0

        for element in counts:
            current = element
            streak_length = 0

            while current in counts:
                streak_length += 1
                current = current * current
            
            max_streak = max(max_streak, streak_length)

        if max_streak > 1:
            return max_streak
        return -1
