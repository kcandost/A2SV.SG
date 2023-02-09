class Solution:
    def maximumSwap(self, num: int) -> int:
        s=str(num)
        a,b=0,0
        i,maxdiff=0,0
        l=len(str(num))
        def diff(i,j):
            return (int(s[j])-int(s[i]))*(10**(l-i-1)-10**(l-j-1))
        
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if j>i:
                    if diff(i,j)>maxdiff:
                        maxdiff=diff(i,j)
                        a,b=i,j
                        
        return num+diff(a,b)
