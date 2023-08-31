class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target - i in numbers:
                num = numbers[::-1]
                z = num.index(target-i)
                return (numbers.index(i)+1 , len(numbers) - z)
