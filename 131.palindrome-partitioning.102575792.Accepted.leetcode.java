public class Solution
{
    public List<List<String>> partition(String s)
    {
        List<List<String>> result = new ArrayList<List<String>>();
        dfs(s, 0, new ArrayList<String>(), result);
        return result;
    }

    private void dfs(String str, int start, ArrayList<String> current, List<List<String>> result)
    {
        if (start == str.length())
        {
            result.add(new ArrayList<String>(current));
        }

        for (int i = start; i < str.length(); i++)
        {
            String subStr = str.substring(start, i + 1);

            if (isPalindrome(subStr))
            {
                current.add(subStr);
                dfs(str, i + 1, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String str)
    {
        int left = 0;
        int right = str.length() - 1;

        while (left < right)
        {
            if (str.charAt(left++) != str.charAt(right--))
            {
                return false;
            }
        }

        return true;
    }
}