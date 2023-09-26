class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        x = []
        seen = set()
        occ = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while x and c < x[-1] and i < occ[x[-1]]:
                    seen.discard(x.pop())
                seen.add(c)
                x.append(c)
        return "".join(x)        
        #NOT MY SOLUTION
