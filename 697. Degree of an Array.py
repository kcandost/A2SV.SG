class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        hash={}
        for idx,num in enumerate(nums):
            #print(idx,num)
            if num not in hash:
                hash.update({num:[1,idx,idx]})
            else:
                hash[num][0]+=1
                hash[num][-1]=idx
        deg,l=0,len(nums)
        for key in hash:
            deg=max(deg,hash[key][0])
        for key in hash:
            if hash[key][0]==deg:
                l=min(l,1+hash[key][2]-hash[key][1])
        
        return l
