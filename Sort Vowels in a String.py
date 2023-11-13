class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowel = "aeiouAEIOU"
        ret = []
        vowels = []

        for element in s:
            if element not in vowel:
                ret.append(element)
            else:
                ret.append("_")
                vowels.append(element)

        vowels = sorted(vowels)
        count = 0

        for element in range(len(ret)):
            if ret[element] == "_":
                ret[element] = vowels[count]
                count += 1

        return "".join(ret)
