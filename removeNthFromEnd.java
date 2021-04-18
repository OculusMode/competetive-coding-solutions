// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// O(N)
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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode z = head, a = head;
        int i = 0;
        while(z.next != null){
            z = z.next;
            if(i<n){
                i++;   
            } else {
                a = a.next;
            }
        }
        if(a.next == null){
            head = null;
        } else if(i<n) {
            head = head.next;
        } else if(a.next.next == null){
            a.next = null;
        } else {
            a.next = a.next.next;
        }
        return head;
    }
}
