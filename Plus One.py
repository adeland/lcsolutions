class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = ["1" , "2" , "3" , "4" ,"5" ,"6" ,"7" ,"8" ,"9" ,"0"]
        digits = str(digits)
        z = ""
        for i in digits:
            if i in nums:
                z += i
            else:
                continue
        z = int(z) + 1
        z = str(z)
        z = list(z)
        count = -1
        for i in z:
            count += 1
            z[count] = int(z[count])
        return z

        
