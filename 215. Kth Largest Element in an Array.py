class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)
        nums=heapq.nlargest(k,nums)# returns k largest elements in descending
        return nums[-1]

        #Below solution has poor time complexity due to sorting at each update

        # i=0
        # arr=[]
        # while i<k:
        #     arr.append(nums[i])
        #     i+=1
        # arr.sort(reverse=True)
        
        # while i<len(nums):
        #     if nums[i]>arr[-1]:
        #         arr.append(nums[i])
        #         arr.sort(reverse=True)
        #         arr.pop(-1)
        #     i+=1
       
        
        # return arr[-1]

     
