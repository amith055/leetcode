class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        j=0
        for i in range(min(len(g),len(s))):
            while j<len(s) and s[j]<g[i] :
                j+=1
            if j<len(s) and s[j]>=g[i]:
                count+=1
                j+=1
        return count