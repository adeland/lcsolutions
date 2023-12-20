```python
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count = 0
        check = money
        prices.sort()

        for price in prices:
            if check - price >= 0:
                count += 1
                check -= price
            if count == 2:
                return check
                
        return money```
