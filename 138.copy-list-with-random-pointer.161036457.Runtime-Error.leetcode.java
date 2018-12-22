public class Solution
{
    private void copyNext(RandomListNode head)
    {
    }

    private void copyRandom(RandomListNode head)
    {
        while (head != null && head.next != null)
        {
            if (head.next.random != null)
            {
                head.next.random = head.random.next;
            }

            head = head.next.next;
        }
    }

    private RandomListNode splitList(RandomListNode head)
    {
        RandomListNode newHead = head.next;

        while (head != null && head.next != null)
        {
            RandomListNode temp = head.next;
            head.next = temp.next;
            head = temp;
        }

        return newHead;
    }

    public RandomListNode copyRandomList(RandomListNode head)
    {
        if (head == null)
        {
            return null;
        }

        copyNext(head);
        copyRandom(head);
        return splitList(head);
    }
}