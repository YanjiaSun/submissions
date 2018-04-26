public class Solution
{
    public List<String> binaryTreePaths(TreeNode root)
    {
        List<String> result = new ArrayList<String>();

        if (root == null)
        {
            return result;
        }

        binaryTreePathsDFS(root, "", result);
        return result;
    }

    void binaryTreePathsDFS(TreeNode root, String out, List<String> result)
    {
        if (root == null)
        {
            return;
        }

        if (out.length() > 0)
        {
            out += "->";
        }

        out += root.val;

        if (root.left == null && root.right == null)
        {
            result.add(out);
            return;
        }

        binaryTreePathsDFS(root.left, out, result);
        binaryTreePathsDFS(root.right, out, result);
    }
}