/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public ListNode deleteDuplicates(ListNode head)
    {
        ListNode node = head;

        while (node != null)
        {
            if (node.val == node.next.val)
            {
                node.next = node.next.next;
            }

            node = node.next;
        }

        return head;
    }
}