class Solution:
    def maxProduct(self, n: int) -> int:
        l1 = [int(x) for x in str(n)]
        l1.sort()

        return l1[-1]*l1[-2]
        