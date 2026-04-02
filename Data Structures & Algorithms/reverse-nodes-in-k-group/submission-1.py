# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        check = head
        for _ in range(k):
            if not check: return head 
            check = check.next
        currHead = head
        prev = nex = None
        p = 0
        
        while currHead and p < k: 
            nex = currHead.next
            currHead.next = prev
            prev = currHead
            currHead = nex
            p += 1
        print(head.next)
        head.next=self.reverseKGroup(currHead,k)
        return prev