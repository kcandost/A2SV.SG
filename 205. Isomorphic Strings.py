class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash={}
        res=True
        for i in range(len(s)):
            if s[i] not in hash:
                if t[i] in hash.values():
                    return False
                else:
                    hash.update({s[i]:t[i]})
            else:
                if hash[s[i]]!=t[i]:
                    return False
                

            
        return res
