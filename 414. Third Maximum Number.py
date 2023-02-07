class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set()
        for num in nums:
           if len(s)<3 :
               s.add(num)
           elif num>min(s) and num not in s:
                s.add(num)
                s.remove(min(s))
        
        if len(s)<3:
            return max(s)

        return min(s)

        # #if the new number is larger than the smallest of smallest
        # #add it to the set and remove the previous
