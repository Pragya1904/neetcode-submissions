class Solution:
    def myPow(self, x: float, n: int) -> float:
        output = 1
        sign = -1 if n < 0 else 1
        power = abs(n)
        while power > 0:
            if (power & 1):
                output *= x
            
            x *= x
            power >>= 1
        
        return 1 / output if sign == -1 else output