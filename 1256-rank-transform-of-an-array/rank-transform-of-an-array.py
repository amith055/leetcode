class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = list(set(arr))
        a.sort()
        d = {val:rnk+1 for rnk,val in enumerate(a)}
        ans = []
        for i in arr:
            ans.append(d[i])
        return ans
        
        
                
        
        