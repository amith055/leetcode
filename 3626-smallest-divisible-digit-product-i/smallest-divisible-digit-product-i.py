class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
       

        while True:
            smallest = n
            n = n+1
            prod = 1
            while smallest >0:
                d = smallest % 10
                prod *= d
                smallest = smallest//10
            if prod % t == 0:
                return n-1