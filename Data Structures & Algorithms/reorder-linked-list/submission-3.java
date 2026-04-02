/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        //reverse linkedlist 
        // connect original to reverse list 
        //find middle 

        if(head==null||head.next==null){
            return;
        }
        ListNode slow = head;
        ListNode prev = null;
        ListNode fast = head;
        while (fast!=null && fast.next!=null){
            prev = slow ;
            slow = slow.next;
            fast=fast.next.next;
        }
        prev.next = null;
        ListNode secondHalf = slow;

        ListNode reversedSecondHalf = reverseList(secondHalf);
        ListNode first = head;
        ListNode second = reversedSecondHalf;
        while (first!=null && second!=null){
            ListNode temp1 = first.next;
            ListNode temp2 = second.next;

            first.next = second; //connect 0->6

            if(temp1!=null){
                second.next=temp1;
            }
            //move foward
            first=temp1;
            second=temp2;
        }



    }
    public ListNode reverseList(ListNode head){
        ListNode prev = null ; 
        ListNode curr = head;
        while(curr!=null){
            ListNode nextNode = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextNode;

        }
        return prev;
    }
}
