class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l=-1
        if s in t:
            return True
        if s.count(s[0])==len(s):
            return t.count(s[0])==len(s)
        for i in range(len(s)):
            if s[i] in t:
               l=t.index(s[i])                
               t=t[l+1:]
            else:
                return False
        return True   