class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []

        for element in range(1, n + 1):

            if element % 3 == 0 and element % 5 == 0:
                ret.append("FizzBuzz")
            elif element % 3 == 0:
                ret.append("Fizz")
            elif element % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(element))
        
        return ret
