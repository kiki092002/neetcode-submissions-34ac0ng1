# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l3  = ListNode(0)
        curr = l3
        sorted_arr = []
        for head in lists:
            temp = head
            #print('list',temp)
            while temp: 
                sorted_arr.append(temp.val)
                #print(temp.val,end='->')
                temp = temp.next
        sorted_arr.sort()
        #print(sorted_arr)
        for val in sorted_arr:
            curr.next = ListNode(val)
            curr = curr.next
        return l3.next
