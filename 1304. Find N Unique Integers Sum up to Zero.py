class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==2: return [-1,1]
        x=[i for i in range(n-1)]
        p=(n-2)*(n-1)//2
        x.append(-p)
        #print(x)
        return x
