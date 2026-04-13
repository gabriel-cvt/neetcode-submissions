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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode runner = new ListNode();
        ListNode finalList = runner;

        ListNode runner1 = list1;
        ListNode runner2 = list2;
        while (runner1 != null && runner2 != null) {
            if (runner1.val <= runner2.val) {
                runner.next = new ListNode(runner1.val);
                runner = runner.next;
                runner1 = runner1.next;
            } else {
                runner.next = new ListNode(runner2.val);
                runner = runner.next;
                runner2 = runner2.next;     
            }
        }

        while (runner1 != null) {
            runner.next = new ListNode(runner1.val);
            runner = runner.next;
            runner1 = runner1.next;
        }

        while (runner2 != null) {
            runner.next = new ListNode(runner2.val);
            runner = runner.next;
            runner2 = runner2.next;
        }
        return finalList.next;
    }
}