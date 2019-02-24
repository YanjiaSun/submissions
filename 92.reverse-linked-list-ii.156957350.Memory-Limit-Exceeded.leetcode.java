public class Solution
{
    public ListNode reverseBetween(ListNode head, int m, int n)
    {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prevM = dummy;
        ListNode prev = null;
        ListNode current = null;
        ListNode post = null;

        for (int i = 1; i <= n; i++)
        {
            if (i < m)
            {
                prevM = prevM.next;
            }
            else if (i == m)
            {
                prev = prevM.next;
                current = prev.next;
            }
            else
            {
                post = current.next;
                current.next = prev;
                prev = current;
                current = post;
            }
        }

        prevM.next = prev;
        return dummy.next;
    }
}
