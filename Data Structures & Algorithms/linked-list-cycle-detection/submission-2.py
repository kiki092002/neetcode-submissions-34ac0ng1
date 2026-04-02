# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            #print(slow.val,fast.val)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print(slow.val,fast.val)
                return True
        return False
        