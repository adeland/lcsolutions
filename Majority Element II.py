class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dic = Counter(nums)
        x = list(dic.keys())
        a = []
        count = 0
        for i in dic.values():
            if i > len(nums) // 3:
                a.append(x[count])
            count += 1
        return a
