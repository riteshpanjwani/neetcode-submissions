class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        d2 = {}
        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1

        if len(d) != len(d2):
            return False
            
        for k, v in d.items():
            if k in d and k not in d2:
                return False
            if k in d2 and k not in d:
                return False
            if k in d and k in d2 and d[k] != d2[k]:
                return False
        return True
        