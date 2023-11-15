class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for element in range(1, len(arr)):
            if arr[element] - arr[element - 1] > 1:
                arr[element] = arr[element - 1] + 1

        return arr[-1]
