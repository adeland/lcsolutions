class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        checks = {}
        
        for number in arr:
            remainder = ((number % k) + k) % k 
            if remainder not in checks:
                checks[remainder] = 1
            else:
                checks[remainder] += 1
        
        for rem in checks:
            if rem == 0:

                if checks[rem] % 2 != 0:
                    return False
            elif rem == k - rem and k % 2 == 0:
                
                if checks[rem] % 2 != 0:
                    return False
            else:
                
                if checks[rem] != checks.get(k - rem, 0):
                    return False
        
        return True
