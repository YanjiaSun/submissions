public class Solution
{
    public List<List<Integer>> levelOrder(TreeNode root)
    {
        List result = new ArrayList();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        if (root != null)
        {
            queue.add(root);
        }

        while (!queue.isEmpty())
        {
            List level = new ArrayList();
            int size = queue.size();

            for (int i = 0; i < size; i++)
            {
                TreeNode node = queue.remove();
                level.add(node.val);

                if (node.left != null)
                {
                    queue.add(node.left);
                }

                if (node.right != null)
                {
                    queue.add(node.right);
                }
            }

            result.add(level);
        }

        return result;
    }
}

