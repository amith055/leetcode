class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0: return 0
        s = 0
        num = ""
        temp = 0
        while n>0:
            d = n % 10
            if d!=0:
                s += d
                num = str(d) + num 
                temp+=1
            n//=10
        return int(num) * s
        