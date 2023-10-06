class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True
        count = 0
        arr = sorted(arr)
        for i in range(len(arr)):
            if i + 2 == len(arr):
                break
            count = arr[i + 1] - arr[i]
            if arr[i + 2] != arr[i] + count + count:
                return False
        return True
