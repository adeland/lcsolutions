class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        z = len(nums) // 3
        x = list(dic.keys())
        y = list(dic.values())
        a = []
        count = -1
        for i in y:
            count += 1
            if i > z:
                a.append(x[count])
        return a
