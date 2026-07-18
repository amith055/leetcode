class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            idx = nums2.index(i)
            nxtg = -1
            for j in range(idx+1,len(nums2)):
                if nums2[j]>i:
                    nxtg = nums2[j]
                    break
            ans.append(nxtg)
        return ans
        