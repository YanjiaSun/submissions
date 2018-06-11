public class Solution
{
    public ListNode detectCycle(ListNode head)
    {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null)
        {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow)
            {
                while (fast != head)
                {
                    fast = fast.next;
                    head = head.next;
                }

                return fast;
            }
        }

        return null;
    }
}
