# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        middle = self.mid(head)
        second_half = middle.next
        middle.next=None
        second_half =  self.reverse(second_half)
        
        # self.printL(head)
        # self.printL(second_half)
        curr = head
        
        while curr and second_half:
            next_node = curr.next #save next node of first half
            curr.next = second_half #link curr node to node from second half
            curr = next_node # move curr forward
            
            temp = second_half.next # save next node of second half
            second_half.next = next_node # link second half node to next node of first half
            second_half=temp #move next node of second half forward
           
        # self.printL(head)



    def mid(self,head):
        s = f = head
        while f and f.next:
            s = s.next
            f= f.next.next
        return s
    def reverse(self,head):
        prev =None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    # def printL(self,head):
    #     curr = head
    #     while curr:
    #         print(curr.val, end=" -> " if curr.next else "\n")
    #         curr = curr.next
        
         