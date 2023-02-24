class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        1) Start rotating deque until the person we are checking is at leftmost
        2)Then until person==0 or len(deque)==1 keep rotating
        """
       
        return sum(min(tickets[k] - (i > k), num) for i, num in enumerate(tickets))
            
            
            
            
            
#         totaltime=0
#         q=deque(tickets)
        
#         #First we let people buy tix and rotate until
#         #the person we want is at the beginning of the deque.
#         i=0
#         while i<k:
#             q[0]-=1
#             totaltime+=1
#             if q[0]==0:
#                 q.popleft()
#             else:
#                 q.rotate(-1)
#             i+=1
#         #Now we start rotating
#         while len(q)>1:
#             for i in range (len(q)):
#                 q[0]-=1
#                 totaltime+=1
#                 if q[0]==0:
#                     q.popleft()
#                 else:
#                     q.rotate(-1)
            
        
        
#         print(q[-1],len(q),q[0]) 
        
            
            
        
