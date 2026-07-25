class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()) : return False
        d={}
        for k,v in zip(pattern,s.split()):
            if k not in d:
                if v in d.values(): return False
                d[k] = v
            elif d[k] !=v:
                return False
        return True
            
        