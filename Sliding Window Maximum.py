class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        r = []
        i = 0
        j = 0
        while(j < len(nums)):
            while len(l) != 0 and l[-1] < nums[j]:
                l.pop()
            l.append(nums[j])
            if j - i + 1 == k:
                r.append(l[0])
                if nums[i] == l[0]:
                    l.pop(0)
                i += 1
            j  += 1
        return r
