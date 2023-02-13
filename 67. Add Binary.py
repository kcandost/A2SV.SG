class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def converted(str):
            res=0
            l=len(str)
            for i in range(l):
                res+=int(str[i])*(2**(l-i-1))
            return res
        return bin(converted(a)+converted(b))[2:]
