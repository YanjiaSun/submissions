public class Solution
{
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode node1, TreeNode node2)
    {
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream

        if (root == null || root == node1 || root == node2)
        {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, node1, node2);
        TreeNode right = lowestCommonAncestor(root.right, node1, node2);

        if (left != null && right != null)
        {
            return root;
        }

        if (left != null)
        {
            return left;
        }

        if (right != null)
        {
            return right;
        }

        == == == =

            if (root == null || root == node1 || root == node2)
        {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, node1, node2);
        TreeNode right = lowestCommonAncestor(root.right, node1, node2);

        if (left != null && right != null)
        {
            return root;
        }

        if (left != null)
        {
            return left;
        }

        if (right != null)
        {
            return right;
        }

        >>> >>> > Stashed changes
        == == == =

            if (root == null || root == node1 || root == node2)
        {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, node1, node2);
        TreeNode right = lowestCommonAncestor(root.right, node1, node2);

        if (left != null && right != null)
        {
            return root;
        }

        if (left != null)
        {
            return left;
        }

        if (right != null)
        {
            return right;
        }

        >>> >>> > Stashed changes
        == == == =

            if (root == null || root == node1 || root == node2)
        {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, node1, node2);
        TreeNode right = lowestCommonAncestor(root.right, node1, node2);

        if (left != null && right != null)
        {
            return root;
        }

        if (left != null)
        {
            return left;
        }

        if (right != null)
        {
            return right;
        }

        >>> >>> > Stashed changes
        == == == =

            if (root == null || root == node1 || root == node2)
        {
            return root;
        }

        TreeNode left = lowestCommonAncestor(root.left, node1, node2);
        TreeNode right = lowestCommonAncestor(root.right, node1, node2);

        if (left != null && right != null)
        {
            return root;
        }

        if (left != null)
        {
            return left;
        }

        if (right != null)
        {
            return right;
        }

        >>> >>> > Stashed changes
        return null;
    }
}
