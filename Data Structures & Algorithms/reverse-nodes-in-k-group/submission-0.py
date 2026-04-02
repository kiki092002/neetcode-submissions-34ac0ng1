# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # find length 
        n = self.length(head)
        dummy = ListNode(0,head)
        prev = dummy
        #reverse k node at a times
        while n >=k:
            curr = prev.next
            nxt = curr.next
            #reverse k group
            for _ in range(k-1):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            # move forward by k step
            prev = curr
            n-=k 
        return dummy.next
    def length(self,head):
        l = 0 
        curr = head
        while curr:
            l+=1
            curr = curr.next
        return l            
