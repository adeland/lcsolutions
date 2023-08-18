class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        numeral=0
        previous_value=1001
        for i in range(len(s)):
            value_of_i = dictionary[s[i]]
            if value_of_i <= previous_value:
                numeral = numeral + value_of_i
                previous_value = value_of_i
            else:
                numeral = numeral + value_of_i - previous_value *2
                previous_value= value_of_i
        return numeral
