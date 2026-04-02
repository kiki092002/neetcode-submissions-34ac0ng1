# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dump = list3 = ListNode()
        run_1 = list1
        run_2 = list2
        while run_1 and run_2:
            if run_1.val <= run_2.val:
                list3.next = run_1
                run_1 = run_1.next
            else:
                list3.next = run_2
                run_2 = run_2.next
            list3 = list3.next
        list3.next = run_1 or run_2
        return dump.next