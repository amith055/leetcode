class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l1 = list(set(nums))
        l1.sort()
        return l1[-3] if len(l1)>=3 else l1[-1]
        