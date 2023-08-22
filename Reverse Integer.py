class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        x = x[::-1]
        count = 0
        if "-" in x:
            x.remove("-")
            for i in x:
                z = x.index(i)
                if i == "0":
                    count += 1
                elif i != "0":
                    break
            n = x[-1]
            x.append(n)
            x = x[count:-1]
            x = x[::-1]
            x.append("-")
            x = x[::-1]
            x = int("".join(x))
            if x not in range(-2**31, 2**31):
                return 0
            return x
        for i in x:
            z = x.index(i)
            if i == "0":
                count += 1
            elif i != "0":
                break
        n = x[-1]
        x.append(n)
        x = x[count:-1]
        x = "".join(x)
        if x == "":
            return 0
        x = int(x)
        if x not in range(-2**31, 2**31):
            return 0
        return x
