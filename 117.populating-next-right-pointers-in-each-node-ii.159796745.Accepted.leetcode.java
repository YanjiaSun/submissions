public class Solution
{
    public void connect(TreeLinkNode root)
    {
        while (root != null)
        {
            TreeLinkNode leftMost = null;
            TreeLinkNode nav = null;

            for (; root != null; root = root.next)
            {
                if (root != null)
                {
                }

                if (leftMost == null)
                {
                    leftMost = root.left != null ? root.left : root.right;
                }

                if (root.left != null)
                {
                    if (nav != null)
                    {
                        nav.next = root.left;
                    }

                    nav = root.left;

                    if (nav != null)
                    {
                    }
                }

                if (root.right != null)
                {
                    if (nav != null)
                    {
                        nav.next = root.right;
                    }

                    nav = root.right;

                    if (nav != null)
                    {
                    }
                }
            }

            root = leftMost;
        }
    }
}
