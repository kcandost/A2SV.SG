class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count=0
        dict={}
        for log in logs:
            if log[-2]!='.':
                count+=1
            elif log=='../':
                count-=1
            count=max(count,0)
        print(logs)

        return count
